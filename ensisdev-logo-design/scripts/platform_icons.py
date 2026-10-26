#!/usr/bin/env python3
"""Export a logo as ready-to-upload icons/banners for game-server and developer platforms.

Presets (run --list-presets):
  minecraft-server-icon  64×64   server-icon.png (Minecraft requires exactly 64×64 PNG; --pixel for blocky art)
  spigot-icon           128×128  resource/plugin icon
  modrinth-icon         512×512  project icon
  hangar-icon           256×256  project icon
  discord-icon          512×512  server icon (shown as a circle: mark kept inside the circle-safe zone)
  discord-banner        960×540  server banner
  github-social        1280×640  repository social preview
  avatar                400×400  generic round-cropped avatar (X, YouTube, Twitch …)
  motd-icon              64×64   alias of minecraft-server-icon (for server list MOTD art)

Sizes are the commonly documented ones; platforms change limits, so confirm on the upload page.

Usage:
  python3 scripts/platform_icons.py logo-symbol.svg --out-dir dist/icons --bg "#0F7C80"
  python3 scripts/platform_icons.py logo-symbol.svg --presets minecraft-server-icon discord-icon --bg "#161616"
  python3 scripts/platform_icons.py logo-symbol.svg --presets minecraft-server-icon --pixel 16 --bg "#161616"
  python3 scripts/platform_icons.py logo-lockup.svg --presets github-social discord-banner --bg "#0B0B0F"
  python3 scripts/platform_icons.py --list-presets

--pixel N  renders the mark on an N×N grid and scales it up with nearest-neighbour, so edges stay crisp pixel
           blocks (needs Pillow). Draw a dedicated pixel version if the mark has fine detail: below ~16 px a
           traced logo turns to mush, a hand-placed pixel silhouette does not.
--circle   adds a *-circle-preview.png for avatar-style presets so you can check the crop before uploading.
"""
import argparse
import os
import sys

sys.dont_write_bytecode = True  # keep the skill folder clean (no __pycache__)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svglib  # noqa: E402,F401
import render_png  # noqa: E402

# name: (width, height, padding fraction per side, circle-cropped?)
PRESETS = {
    "minecraft-server-icon": (64, 64, 0.06, False),
    "motd-icon": (64, 64, 0.06, False),
    "spigot-icon": (128, 128, 0.10, False),
    "modrinth-icon": (512, 512, 0.12, False),
    "hangar-icon": (256, 256, 0.12, False),
    "discord-icon": (512, 512, 0.20, True),
    "discord-banner": (960, 540, 0.22, False),
    "github-social": (1280, 640, 0.20, False),
    "avatar": (400, 400, 0.20, True),
}


def pixelate(png, out, size, grid, pil):
    im = pil.open(png).convert("RGBA")
    im = im.resize((grid, grid), pil.NEAREST) if im.size != (grid, grid) else im
    im.resize((size, size), pil.NEAREST).save(out)


def circle_preview(png, out, pil):
    im = pil.open(png).convert("RGBA")
    mask = pil.new("L", im.size, 0)
    from PIL import ImageDraw  # noqa: E402
    ImageDraw.Draw(mask).ellipse((0, 0, im.size[0] - 1, im.size[1] - 1), fill=255)
    cut = pil.new("RGBA", im.size, (0, 0, 0, 0))
    cut.paste(im, (0, 0), mask)
    cut.save(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("svg", nargs="?", help="master SVG (symbol for square presets, lockup for banners)")
    ap.add_argument("--presets", nargs="*", help="subset of presets (default: all)")
    ap.add_argument("--out-dir", default="platform-icons")
    ap.add_argument("--name", help="file name prefix (default: SVG file name)")
    ap.add_argument("--bg", help="background colour, e.g. '#161616' (default: transparent; Minecraft/Discord look best filled)")
    ap.add_argument("--pixel", type=int, metavar="N", help="pixel-art mode: render on an N×N grid, scale up with nearest-neighbour")
    ap.add_argument("--circle", action="store_true", help="also write a circle-crop preview for avatar-style presets")
    ap.add_argument("--list-presets", action="store_true")
    a = ap.parse_args()

    if a.list_presets:
        for k, (w, h, pad, circ) in PRESETS.items():
            print(f"{k:24s}{w}×{h}  padding {int(pad * 100)}%{'  (circle-cropped by the platform)' if circ else ''}")
        return
    if not a.svg:
        ap.error("an SVG is required (or use --list-presets)")
    pil = None
    if a.pixel or a.circle:
        try:
            import PIL.Image as pil  # noqa: N813
        except ImportError:
            sys.exit("--pixel/--circle need Pillow (pip install pillow)")
    names = a.presets or list(PRESETS)
    bad = [n for n in names if n not in PRESETS]
    if bad:
        sys.exit(f"unknown preset(s): {', '.join(bad)} (see --list-presets)")
    if not render_png.available_backends():
        sys.exit("no rendering backend (see: python3 scripts/render_png.py --which)")

    os.makedirs(a.out_dir, exist_ok=True)
    base = a.name or os.path.splitext(os.path.basename(a.svg))[0]
    for n in names:
        w, h, pad, circ = PRESETS[n]
        out = os.path.join(a.out_dir, "server-icon.png" if n == "minecraft-server-icon" and not a.name
                           else f"{base}-{n}.png")
        pixel = a.pixel and w == h and w <= 128
        if pixel:
            tmp = out + ".grid.png"
            ok = render_png.render(a.svg, tmp, a.pixel, a.pixel, pad, a.bg)
            if ok:
                pixelate(tmp, out, w, a.pixel, pil)
                os.remove(tmp)
        else:
            ok = render_png.render(a.svg, out, w, h, pad, a.bg)
        if not ok:
            print(f"skipped {n}: render failed")
            continue
        print("wrote", out, f"({w}×{h})")
        if a.circle and circ:
            prev = out[:-4] + "-circle-preview.png"
            circle_preview(out, prev, pil)
            print("wrote", prev)


if __name__ == "__main__":
    main()
