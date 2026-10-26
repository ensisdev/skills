# Notice

`ensisdev-logo-design` is derived from [kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)
(v1.4.5, MIT License, Copyright (c) 2026 kaankiziltug) — see `LICENSE`, which retains the original copyright notice.

## Changes from upstream

- Renamed to `ensisdev-logo-design`; single-skill layout without the plugin/marketplace packaging.
- Added `references/game-dev-branding.md` (Minecraft servers/plugins, Discord and developer-platform assets,
  pixel-grid construction, dark-first colour).
- Added `scripts/platform_icons.py` (server-icon.png, Spigot/Modrinth/Hangar, Discord, GitHub social, avatars,
  `--pixel` grid mode, circle-crop preview) and `scripts/fetch_library.py`.
- `render_png.py`: finds Playwright/Chromium headless shells, honours `CHROME_PATH`, runs as root in containers.
- Reference logos are **not bundled**. The catalog (`assets/library/catalog.json`, `classifications.json`,
  `stats.json`) is kept; the SVG files are third-party trademarks and can be downloaded for study with
  `scripts/fetch_library.py`. Their inclusion upstream is nominative/educational; the MIT license does not cover them.
- New eval (Minecraft server branding) and a smoke test adapted to this layout (`python3 tools/smoke_test.py`).
