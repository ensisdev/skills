#!/usr/bin/env python3
"""ensisdev-mc-design message linter.

Scans Java/Kotlin sources and YAML/properties message files for the mechanically
checkable rules in rules/lint_rules.yaml. Read-only, stdlib only.

    python -I tools/lint_messages.py <path> [<path> ...] [--fail-on ERROR|WARN|INFO]

Results are heuristics (regex over lines), not a parser: expect rare false
positives/negatives. Suppress one line with the text `lint:ignore` in a comment
on that line. Rules that need cross-screen judgment (GUI-*, VAR-*, LORE-001,
COLOR-*) stay manual: see qa/DESIGN_VALIDATION.md.
"""
import argparse
import os
import re
import sys

CODE_EXT = {".java", ".kt", ".kts"}
DATA_EXT = {".yml", ".yaml", ".properties"}
SKIP_DIRS = {".git", "build", "target", "out", ".gradle", "node_modules", "fixtures_ignore"}

SEV_ORDER = {"ERROR": 3, "WARN": 2, "INFO": 1}

DECOR = set("✦★◆❖✧»«➜▸◇✪❂")
PAIR_GLYPHS = set("✦★◆❖✧»«")
SMALL_CAPS = set("ᴀʙᴄᴅᴇꜰғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀᴛᴜᴠᴡʏᴢ")  # s and x have no distinct small-cap form
TR_SPECIAL = set("çğöşüÇĞÖŞÜ")

STRING_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')
TAGS = r"(?:<[^>]+>)*"
CLOSE_TAGS = r"(?:</[^>]+>)*"
SEPARATORS = r"(?:»|>>|\||➜|→|◆|▸|›|:|-|–|—)"
PREFIX_SEP_RE = re.compile(r"^\s*" + TAGS + r"\[[^\]\n]{1,24}\]" + CLOSE_TAGS + r"\s*" + SEPARATORS)
GRAD_PREFIX_RE = re.compile(r"<gradient:([^>]+)>\s*\[[^\]\n]{1,24}\]\s*</gradient>")
GRADIENT_RE = re.compile(r"<gradient:([^>]+)>")
DESERIALIZE_BAD_RE = re.compile(
    r"deserialize\s*\(\s*(?:"
    r'"[^"]*"\s*\+'                      # "..." + x
    r'|[A-Za-z_][\w.]*\s*\+\s*"'          # x + "..."
    r'|"[^"]*\$\{?(?!Theme\b|[A-Z_]{2,}\b)\w'   # kotlin template with non-constant
    r"|String\.format"
    r"|.*\.formatted\("
    r")"
)
PAD_RE = re.compile(r'(?:" "\.repeat\(|StringUtils\.repeat\(\s*" "|String\.format\(\s*"[^"]*%-?\d+s|\.padEnd\(|\.padStart\()')
LEGACY_RE = re.compile(r"§|ChatColor\.|translateAlternateColorCodes")
CASE_RE = re.compile(r"\.to(?:Upper|Lower)Case\(\s*\)")
SEND_RE = re.compile(r"\.send(?:Rich)?Message\(")
CHAT_DEFINER_RE = re.compile(r"\b(?:object|class)\s+Chat\b")
PREFIX_USE_RE = re.compile(r"Chat\.send|Lang\.send|prefix|Prefix|PREFIX")


class Finding:
    def __init__(self, path, line, sev, rid, msg):
        self.path, self.line, self.sev, self.rid, self.msg = path, line, sev, rid, msg

    def __str__(self):
        return f"{self.path}:{self.line}: [{self.sev}] {self.rid} {self.msg}"


def iter_files(paths):
    for root in paths:
        if os.path.isfile(root):
            yield root
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for f in sorted(filenames):
                if os.path.splitext(f)[1].lower() in CODE_EXT | DATA_EXT:
                    yield os.path.join(dirpath, f)


def read_lines(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read().splitlines()


def strings_in_line(line, ext):
    if ext in CODE_EXT:
        return [m.group(1) for m in STRING_RE.finditer(line)]
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return []
    if ext == ".properties":
        value = stripped.split("=", 1)[1] if "=" in stripped else ""
    else:
        if stripped.startswith("- "):
            value = stripped[2:]
        elif ": " in stripped:
            value = stripped.split(": ", 1)[1]
        else:
            value = ""
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return [value] if value else []


def longest_small_caps_run(s):
    best = cur = 0
    for ch in s:
        if ch in SMALL_CAPS or (cur and ch in " s"):
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return best


def check_string(text, path, n, out, prefix_literals):
    # PREFIX-002 separator after prefix
    if PREFIX_SEP_RE.search(text):
        out.append(Finding(path, n, "WARN", "PREFIX-002", "separator or glyph after the [Plugin] prefix: use a single space"))
    # PREFIX-003 stops + collect literals
    for m in GRADIENT_RE.finditer(text):
        stops = [p for p in m.group(1).split(":") if p]
        if len(stops) > 3:
            out.append(Finding(path, n, "WARN", "PREFIX-003", f"gradient has {len(stops)} stops (max 3)"))
    pm = GRAD_PREFIX_RE.search(text)
    if pm:
        prefix_literals.append((path, n, pm.group(0)))
    # GLYPH-001 paired glyphs surrounding a title
    plain = re.sub(r"<[^>]+>", "", text).strip()
    if len(plain) >= 3 and plain[0] in PAIR_GLYPHS and plain[-1] in PAIR_GLYPHS:
        out.append(Finding(path, n, "ERROR", "GLYPH-001", f"decorative glyphs surround text: {plain[:40]!r}"))
    # GLYPH-004 too many decorative glyphs
    if sum(1 for ch in plain if ch in DECOR) >= 3:
        out.append(Finding(path, n, "INFO", "GLYPH-004", "more than two decorative glyphs in one string"))
    # LORE-003 long small caps
    if longest_small_caps_run(plain) > 24:
        out.append(Finding(path, n, "INFO", "LORE-003", "long text set in small caps (>24 chars)"))
    # TR-001 small-cap word containing Turkish special letters
    for token in re.split(r"\s+", plain):
        if sum(1 for ch in token if ch in SMALL_CAPS) >= 2 and any(ch in TR_SPECIAL for ch in token):
            out.append(Finding(path, n, "WARN", "TR-001", f"small-caps word mixes normal ç/ğ/ö/ş/ü: {token!r}"))
            break


def lint(paths):
    out, prefix_literals = [], []
    scanned = 0
    for path in iter_files(paths):
        ext = os.path.splitext(path)[1].lower()
        lines = read_lines(path)
        scanned += 1
        is_chat_definer = ext in CODE_EXT and any(CHAT_DEFINER_RE.search(l) for l in lines)
        for n, line in enumerate(lines, 1):
            if "lint:ignore" in line:
                continue
            if ext in CODE_EXT:
                stripped = line.strip()
                if stripped.startswith(("//", "*", "/*")):
                    continue
                code = STRING_RE.sub('""', line).split("//")[0]   # identifiers only: no strings, no trailing comment
                if SEND_RE.search(code) and not is_chat_definer and not PREFIX_USE_RE.search(code):
                    out.append(Finding(path, n, "ERROR", "PREFIX-001", "direct sendMessage without the standard prefix (use Chat.send); heuristic"))
                if DESERIALIZE_BAD_RE.search(line):
                    out.append(Finding(path, n, "ERROR", "DATA-001", "MiniMessage string built by concatenation/template; use Placeholder.unparsed/component"))
                if PAD_RE.search(line):
                    out.append(Finding(path, n, "WARN", "DATA-002", "padding/width assumption: proportional font, do not align with spaces"))
                if CASE_RE.search(line):
                    out.append(Finding(path, n, "WARN", "TR-002", "no-arg toUpperCase()/toLowerCase(): pass Locale.ROOT (identifiers) or the player's locale (display)"))
            if LEGACY_RE.search(line):
                out.append(Finding(path, n, "WARN", "COMPAT-001", "legacy section-sign / ChatColor formatting: use MiniMessage/Adventure"))
            for s in strings_in_line(line, ext):
                check_string(s, path, n, out, prefix_literals)

    # PREFIX-003 across files: prefix literal duplicated or inconsistent
    distinct = {lit for _, _, lit in prefix_literals}
    if len(distinct) > 1:
        for path, n, lit in prefix_literals[1:]:
            if lit != prefix_literals[0][2]:
                out.append(Finding(path, n, "WARN", "PREFIX-003", f"prefix differs from the first one found ({prefix_literals[0][0]}:{prefix_literals[0][1]})"))
    elif len(prefix_literals) > 1:
        for path, n, _ in prefix_literals[1:]:
            out.append(Finding(path, n, "WARN", "PREFIX-003", "prefix literal repeated; build it once (Chat.prefix) and reuse"))
    return out, scanned


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--fail-on", choices=["ERROR", "WARN", "INFO"], default="ERROR",
                    help="exit 1 when a finding of this severity or higher exists (default ERROR)")
    args = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")   # Windows consoles are not UTF-8
    findings, scanned = lint(args.paths)
    findings.sort(key=lambda f: (f.path, f.line, -SEV_ORDER[f.sev]))
    for f in findings:
        print(f)
    counts = {s: sum(1 for f in findings if f.sev == s) for s in SEV_ORDER}
    print(f"\nscanned {scanned} file(s): {counts['ERROR']} ERROR, {counts['WARN']} WARN, {counts['INFO']} INFO")
    worst = max((SEV_ORDER[f.sev] for f in findings), default=0)
    return 1 if worst >= SEV_ORDER[args.fail_on] else 0


if __name__ == "__main__":
    sys.exit(main())
