#!/usr/bin/env python3
"""Download the reference-logo SVG files (assets/library/svg/) from the upstream project.

This skill ships only the searchable catalog (catalog.json, classifications.json, stats.json): the logos themselves
are third-party trademarks and are not redistributed here. `search_library.py` works from the catalog alone; run this
script when you want to *read the SVG source* of reference logos (`--format paths`, shelf tests, technique study).

  python3 scripts/fetch_library.py            # shallow-clone upstream, copy svg/ into assets/library/svg/
  python3 scripts/fetch_library.py --check    # report whether the files are present

Needs git and network access. Files are for study only (see the trademark note in SKILL.md / NOTICE.md).
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True  # keep the skill folder clean (no __pycache__)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svglib  # noqa: E402

UPSTREAM = "https://github.com/kaankiziltug/logo-design-skill"
SUBDIR = os.path.join("skills", "logo-design", "assets", "library", "svg")


def count():
    d = svglib.LIBRARY_SVG_DIR
    return len([f for f in os.listdir(d) if f.lower().endswith(".svg")]) if os.path.isdir(d) else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--force", action="store_true", help="re-download even if files are present")
    a = ap.parse_args()
    have = count()
    if a.check:
        print(f"{have} reference SVGs in {svglib.LIBRARY_SVG_DIR}")
        return
    if have and not a.force:
        print(f"already present: {have} SVGs (use --force to re-download)")
        return
    if not shutil.which("git"):
        sys.exit("git not found")
    with tempfile.TemporaryDirectory() as tmp:
        env = dict(os.environ, GIT_LFS_SKIP_SMUDGE="1")
        r = subprocess.run(["git", "clone", "--depth", "1", "--filter=blob:none", "--sparse", UPSTREAM, tmp + "/up"],
                           env=env, capture_output=True, text=True)
        if r.returncode == 0:
            r = subprocess.run(["git", "-C", tmp + "/up", "sparse-checkout", "set", SUBDIR.replace(os.sep, "/")],
                               env=env, capture_output=True, text=True)
        src = os.path.join(tmp, "up", SUBDIR)
        if r.returncode != 0 or not os.path.isdir(src):
            sys.exit("download failed: " + (r.stderr.strip() or "svg folder not found upstream"))
        os.makedirs(svglib.LIBRARY_SVG_DIR, exist_ok=True)
        for f in os.listdir(src):
            shutil.copy2(os.path.join(src, f), svglib.LIBRARY_SVG_DIR)
    print(f"fetched {count()} SVGs into {svglib.LIBRARY_SVG_DIR}")


if __name__ == "__main__":
    main()
