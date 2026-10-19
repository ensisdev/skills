#!/usr/bin/env python3
"""Generate a self-contained illustrative Minecraft sidebar/TAB preview and compact report."""
import argparse
import html
import json
import re
import sys
from pathlib import Path

HEX = re.compile(r"^#[0-9a-fA-F]{6}$")
ORNAMENT = re.compile(r"[★☆✦✧◆◇●•▰▱❖❈✨🌟⭐]")
EMOJI = re.compile(r"[\U0001F300-\U0001FAFF]")
PLACEHOLDER = re.compile(r"%[^%\s]+%|\{[a-zA-Z_][\w.:-]*\}")
# Letters with no reliable Unicode small-cap equivalent. Never silently
# transliterate these; use ordinary text or a tested custom font instead.
NO_SMALLCAPS = re.compile(r"[İıŞşĞğÇçÖöÜüqQ]")


def esc(value):
    return html.escape(str(value), quote=True)


def color(value, default):
    return value if isinstance(value, str) and HEX.fullmatch(value) else default


def plain(value):
    if isinstance(value, list):
        return "".join(str(x.get("fallback", x.get("text", ""))) if isinstance(x, dict) else str(x) for x in value)
    return str(value or "")


def smallcaps_text(value):
    """Raw text of segments flagged small_caps (visual hint in preview)."""
    if isinstance(value, dict):
        value = value.get("segments", value.get("text", ""))
    if not isinstance(value, list):
        return ""
    return "".join(str(x.get("text", "")) for x in value if isinstance(x, dict) and x.get("small_caps"))


def rich(value, default="text"):
    if isinstance(value, dict):
        value = value.get("segments", value.get("text", ""))
    if not isinstance(value, list):
        return '<span class="%s">%s</span>' % (default, esc(plain(value)))
    parts = []
    for item in value:
        if not isinstance(item, dict):
            parts.append(esc(item))
            continue
        if "sprite" in item:
            parts.append('<span class="sprite" title="Sprite approximation: %s">%s</span>' %
                         (esc(item["sprite"]), esc(item.get("fallback", "▣"))))
            continue
        styles = []
        if HEX.fullmatch(str(item.get("color", ""))):
            styles.append("color:" + item["color"])
        if item.get("bold"):
            styles.append("font-weight:700")
        if item.get("shadow"):
            styles.append("text-shadow:1px 1px 0 #000")
        classes = "smallcaps" if item.get("small_caps") else default
        parts.append('<span class="%s" style="%s">%s</span>' %
                     (classes, esc(";".join(styles)), esc(item.get("text", ""))))
    return "".join(parts)


def validate(data):
    problems = []
    if not isinstance(data, dict):
        return ["Root must be a JSON object"]
    if not isinstance(data.get("sidebar"), dict) or not isinstance(data.get("tab"), dict):
        problems.append("sidebar and tab must be objects")
    rows = data.get("sidebar", {}).get("rows", []) if isinstance(data.get("sidebar"), dict) else []
    if not isinstance(rows, list) or any(not isinstance(r, dict) for r in rows):
        problems.append("sidebar.rows must be an array of objects")
    if len(rows) > 18:
        problems.append("sidebar has more than 18 rows; likely crowded")
    tab = data.get("tab", {})
    if isinstance(tab, dict):
        for key in ("header", "footer", "groups"):
            if not isinstance(tab.get(key, []), list):
                problems.append("tab.%s must be an array" % key)
    return problems


def row_html(row):
    kind = row.get("kind", "text")
    if kind == "space":
        return '<div class="row spacer" aria-hidden="true"></div>'
    if kind == "separator":
        return '<div class="row separator">%s</div>' % rich(row.get("text", ""))
    if kind == "stat":
        return '<div class="row stat"><span class="label">%s</span><span class="value">%s</span></div>' % (
            rich(row.get("label", ""), "muted"), rich(row.get("value", "")))
    return '<div class="row %s">%s</div>' % ("footer" if kind == "footer" else "", rich(row.get("text", "")))


def line_html(line):
    return '<div class="tabline">%s</div>' % rich(line)


def assess(data, issues):
    sidebar = data.get("sidebar", {})
    tab = data.get("tab", {})
    rows = sidebar.get("rows", [])
    visible = [r for r in rows if r.get("kind") != "space"]
    all_text = [plain(sidebar.get("title", ""))]
    for r in visible:
        all_text.extend((plain(r.get("label", "")), plain(r.get("value", r.get("text", "")))))
    all_text += [plain(x) for x in tab.get("header", []) + tab.get("footer", [])]
    all_text += [plain(g.get("name", "")) for g in tab.get("groups", []) if isinstance(g, dict)]
    joined = " ".join(all_text)
    longest = max(map(len, all_text), default=0)
    ornaments = len(ORNAMENT.findall(joined))
    emoji = len(EMOJI.findall(joined))
    placeholders = PLACEHOLDER.findall(joined)
    sc_texts = [smallcaps_text(sidebar.get("title", ""))]
    for r in visible:
        sc_texts.append(smallcaps_text(r.get("label", "")))
        sc_texts.append(smallcaps_text(r.get("value", r.get("text", ""))))
    sc_texts += [smallcaps_text(x) for x in tab.get("header", []) + tab.get("footer", [])]
    risky_sc = sorted(set("".join(NO_SMALLCAPS.findall(" ".join(sc_texts)))))
    compat = data.get("compatibility", {})
    verified = bool(compat.get("parser_verified") and compat.get("glyphs_verified") and compat.get("in_game_verified"))
    signals = []
    if len(visible) > 10: signals.append("Sidebar may be too tall")
    if longest > 36: signals.append("A line may overflow at narrow GUI scale")
    if ornaments > 3: signals.append("Repeated ornament symbols")
    if emoji: signals.append("Emoji require in-game glyph verification")
    if risky_sc: signals.append("Small caps with unsupported glyphs (%s): verify in-game or use plain text" % ", ".join(risky_sc))
    if placeholders: signals.append("Placeholder provider and expansion need verification")
    if issues: signals.extend(issues)
    score = {
        "usefulness": 2 if 2 <= len(visible) <= 8 else 1 if visible else 0,
        "hierarchy": 2 if sidebar.get("title") and any(r.get("kind") == "space" for r in rows) else 1 if sidebar.get("title") else 0,
        "restraint": 2 if ornaments <= 1 and emoji == 0 else 1 if ornaments <= 3 and emoji <= 1 else 0,
        "legibility": 2 if longest <= 26 and len(visible) <= 9 else 1 if longest <= 36 and len(visible) <= 12 else 0,
        "compatibility": 2 if verified and not placeholders and not emoji else 1 if isinstance(compat, dict) and compat else 0,
    }
    return {"provisional_score": sum(score.values()), "dimensions": score,
            "signals": signals, "measures": {"sidebar_rows": len(visible), "longest_text_characters": longest,
                                      "ornament_count": ornaments, "emoji_count": emoji,
                                      "smallcaps_risky_characters": "".join(risky_sc)},
            "caveat": "Automated surface check; review usefulness and verify rendering in Minecraft."}


def render(data, report):
    sidebar = data["sidebar"]
    tab = data["tab"]
    palette = data.get("palette", {})
    accent = color(palette.get("accent"), "#67D4AF")
    ink = color(palette.get("text"), "#F2F5EF")
    muted = color(palette.get("muted"), "#AAB7AE")
    rows = "\n".join(row_html(x) for x in sidebar.get("rows", []))
    headers = "\n".join(line_html(x) for x in tab.get("header", []))
    footers = "\n".join(line_html(x) for x in tab.get("footer", []))
    groups = []
    for group in tab.get("groups", []):
        if not isinstance(group, dict): continue
        players = "".join('<div class="player"><span>%s</span><span class="ping">▂▄▆</span></div>' % rich(p)
                          for p in group.get("players", []))
        groups.append('<section class="group"><h3>%s</h3>%s</section>' % (esc(group.get("name", "")), players))
    notes = "".join("<li>%s</li>" % esc(n) for n in data.get("implementation_notes", []))
    assumptions = "".join("<li>%s</li>" % esc(a) for a in data.get("assumptions", []))
    if not assumptions:
        assumptions = "<li>None recorded.</li>"
    signals = "".join("<li>%s</li>" % esc(s) for s in report["signals"])
    return '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s — Minecraft layout prototype</title><style>
:root{--accent:%s;--ink:%s;--muted:%s}*{box-sizing:border-box}body{margin:0;background:#111b1c;color:#e8f0e9;font:14px system-ui,Arial,sans-serif}
header{max-width:1200px;margin:auto;padding:22px 24px 12px;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}h1{font-size:20px;margin:0 0 4px}header p{margin:0;color:#aab7b0}.controls{display:flex;gap:8px}button{background:#223431;color:white;border:1px solid #537b6b;padding:8px 14px;border-radius:7px;cursor:pointer}button[aria-pressed=true]{background:#3d806b}
.frame{position:relative;width:min(1152px,calc(100%% - 32px));aspect-ratio:16/9;margin:16px auto 26px;overflow:hidden;border:1px solid #728f76;box-shadow:0 24px 70px #0008;background:linear-gradient(#7297aa 0 45%%,#c4c9aa 46%% 51%%,#527f50 52%% 60%%,#335b3d 61%% 100%%)}
.frame:before{content:"";position:absolute;inset:45%% 0 0;background:linear-gradient(151deg,transparent 0 14%%,#416744 14%% 26%%,transparent 26%%),linear-gradient(18deg,transparent 0 17%%,#284d39 17%% 30%%,transparent 30%%),repeating-linear-gradient(0deg,#0001 0 3px,transparent 3px 8px);opacity:.9}.frame:after{content:"";position:absolute;bottom:-4%%;left:8%%;width:62%%;height:30%%;background:linear-gradient(25deg,#746d50 0 21%%,#506649 21%% 100%%);clip-path:polygon(0 100%%,30%% 24%%,60%% 53%%,82%% 0,100%% 100%%);opacity:.7}
.hud{position:relative;z-index:1;width:100%%;height:100%%;font-family:ui-monospace,'Courier New',monospace;font-size:clamp(9px,1.25vw,15px);font-weight:600;line-height:1.4;color:var(--ink);text-shadow:1px 1px 0 #000}.crosshair{position:absolute;left:50%%;top:50%%;transform:translate(-50%%,-50%%);font-size:23px;color:#fff9}.hotbar{position:absolute;bottom:4%%;left:50%%;transform:translateX(-50%%);display:flex;gap:2px}.slot{width:29px;height:29px;background:#222a;border:2px solid #bbb8}.slot:first-child{border-color:#fff}
.sidebar{position:absolute;right:2.4%%;top:28%%;min-width:174px;max-width:32%%;background:#151c19a6;padding:7px 9px;box-shadow:0 3px 15px #0004}.sidebar-title{text-align:center;color:var(--accent);font-weight:800;letter-spacing:.05em;margin-bottom:5px}.row{min-height:1.35em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.stat{display:flex;justify-content:space-between;gap:14px}.label,.muted,.footer{color:var(--muted)}.value{color:var(--ink);text-align:right}.spacer{height:.65em;min-height:0}.separator{color:var(--muted);opacity:.7}.smallcaps{letter-spacing:.03em}.sprite{border:1px dashed var(--accent);border-radius:2px;padding:0 2px;color:var(--accent)}
.tab{display:none;position:absolute;left:50%%;top:8%%;transform:translateX(-50%%);width:min(70%%,620px);max-height:82%%;overflow:auto;text-align:center;background:#191e1bdc;border:1px solid #c4d6c096;padding:12px 18px;box-shadow:0 8px 30px #0009}.tabline{min-height:1.4em}.tabhead{color:var(--accent);margin-bottom:9px}.tabfoot{color:var(--muted);margin-top:9px}.players{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;text-align:left}.group h3{font-size:inherit;color:var(--muted);margin:0 0 4px;border-bottom:1px solid #8aa89966}.player{display:flex;justify-content:space-between;gap:8px;padding:2px 4px;background:#ffffff0d;white-space:nowrap;overflow:hidden}.ping{color:#77c95a}.tab-open .tab{display:block}.tab-open .sidebar{opacity:.3}
.narrow{width:min(700px,calc(100%% - 32px))}.narrow .sidebar{right:1.5%%;top:19%%;max-width:40%%;min-width:130px;padding:4px;font-size:9px}.narrow .tab{width:85%%;font-size:10px;padding:7px}.narrow .slot{width:18px;height:18px}
.below{max-width:1152px;margin:0 auto 40px;padding:0 20px;display:grid;grid-template-columns:1fr 1fr;gap:18px}.card{border:1px solid #40564c;background:#192923;border-radius:9px;padding:15px 19px}.card h2{font-size:15px;margin:0 0 8px}.card p{margin:4px 0;color:#c4d1c6}li{margin:4px 0;color:#c4d1c6}code{color:#92dabb}@media(max-width:680px){.below{grid-template-columns:1fr}.frame{width:calc(100%% - 12px)}.sidebar{font-size:8px;min-width:100px;padding:3px}.tab{font-size:8px}.slot{width:14px;height:14px}}
</style></head><body><header><div><h1>%s · %s</h1><p>Illustrative in-game layout prototype · fonts and glyphs require Minecraft verification</p></div><div class="controls"><button id="view" aria-pressed="false">Show TAB</button><button id="size" aria-pressed="false">Narrow view</button></div></header>
<main class="frame" id="frame"><div class="hud"><div class="crosshair">+</div><div class="sidebar"><div class="sidebar-title">%s</div>%s</div><div class="tab"><div class="tabhead">%s</div><div class="players">%s</div><div class="tabfoot">%s</div></div><div class="hotbar">%s</div></div></main>
<div class="below"><section class="card"><h2>Provisional review · %s/10</h2><p>Surface checks only; judge player value and confirm in-game rendering.</p><ul>%s</ul></section><section class="card"><h2>Implementation notes</h2><ul>%s</ul></section><section class="card"><h2>Assumptions (unverified)</h2><ul>%s</ul></section></div>
<script>for(const [id,cls,labels] of [['view','tab-open',['Show TAB','Show sidebar']],['size','narrow',['Narrow view','Wide view']]]){const b=document.getElementById(id),f=document.getElementById('frame');b.onclick=()=>{const on=f.classList.toggle(cls);b.setAttribute('aria-pressed',String(on));b.textContent=labels[Number(on)]}}</script></body></html>''' % (
        esc(data.get("server", "Server")), accent, ink, muted,
        esc(data.get("server", "Server")), esc(data.get("mode", "")), rich(sidebar.get("title", "")), rows,
        headers, "".join(groups), footers, '<div class="slot"></div>' * 9,
        report["provisional_score"], signals or '<li>No surface warnings; check the design in-game.</li>', notes or '<li>No notes supplied.</li>', assumptions)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input", type=Path)
    ap.add_argument("-o", "--output", type=Path, required=True)
    ap.add_argument("--report", type=Path)
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        issues = validate(data)
        if any("must be" in x for x in issues) or (issues and args.strict):
            raise ValueError("; ".join(issues))
        report = assess(data, issues)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(render(data, report), encoding="utf-8")
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"html": str(args.output), "score": report["provisional_score"], "signals": report["signals"]}, ensure_ascii=False))
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print("preview: " + str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
