# Game-server & developer-platform branding

Load this when the logo is for a Minecraft server/network/plugin/mod/resource pack, a Discord community, or any
asset that will live as a tiny square on a platform you don't control. The general rules still apply
(`principles.md`, `testing-checklist.md`); this file adds what is specific to these surfaces.

## 1. The reality: your logo is a 64 px square

Where these logos are actually seen, most to least:

| Surface | Real size | Notes |
|---|---|---|
| Minecraft server list (`server-icon.png`) | 64×64, exactly | Next to a MOTD, on a dark UI, often scaled down by the launcher |
| Discord server/avatar | 512 source, shown 32–96 px, **circle crop** | Corners are lost; mark must sit inside the circle |
| Plugin/mod listing (Spigot, Modrinth, Hangar, CurseForge) | 128–512 source, shown 48–96 px in a dense list | Competes with dozens of near-identical icons |
| GitHub repo / social preview | 1280×640 card, shown small in link unfurls | Needs a wide lockup; text must survive 400 px width |
| Server banner / header | wide, 960×540-ish | The only place a full wordmark has room |

Design the **symbol at 32 px first**; the lockup comes second. Verify with `preview_sheet.py` (16/32 px pixel test)
and `platform_icons.py --circle`. Limits change: confirm each platform's current size/format rules on its upload page.

## 2. Pixel-grid construction (when the brand is blocky)

Minecraft-adjacent audiences read pixel/voxel language instantly — which is also why it is the biggest cliché.
Use it only as a *construction method*, not as a costume.

- Pick the grid before drawing: **16×16** for a 64 px icon (each cell = 4 px), 32×32 for banners. Never mix grid
  sizes inside one mark.
- Place squares by hand on integer cells. In SVG: `<rect width="1" height="1">` units with `viewBox="0 0 16 16"`
  and `shape-rendering="crispEdges"`. No rotated or half-cell shapes.
- Silhouette first: if the mark isn't recognisable as a one-colour blob on the grid, shading won't save it.
- Limit to 3–4 colours: base, one shade, one highlight, one outline/accent. Shade by hue shift, not just lightness.
- Dithering and 1-cell details die at server-list scale; keep every feature ≥ 2 cells.
- Export with `platform_icons.py --pixel 16`; it scales with nearest-neighbour so cells stay sharp. Never export
  pixel art through a smoothing resize.
- A pixel mark needs a **non-pixel companion** for large uses (banner, merch) — pair it with a clean geometric
  wordmark, or the brand will look like every other server.

## 3. Avoiding the genre's clichés

Name the category defaults and then choose consciously:

- Server clichés: crossed swords, shields, crowns, grass-block cubes, creeper faces, flaming skulls, gradient
  "cyber" letterforms, glow + drop shadow. Plugin clichés: gear, puzzle piece, wrench, magic wand, anvil.
- Prefer **one ownable idea from the name or the gameplay loop** (a Skyblock server → the island/void gap as
  negative space; a economy plugin → a coin whose centre is the plugin's initial) over a generic icon of the genre.
- Distinct silhouette beats distinct colour: recolouring a stock cube is not a logo. Test the silhouette in
  black on white at 32 px — could another server's icon be mistaken for it?
- Never use Minecraft's logo, Creeper face, official textures, item sprites or the Mojang/Microsoft name in the mark.
  Cube/voxel *geometry* and pixel *technique* are fine; recreated official assets are not. Say "unofficial/unaffiliated"
  in the guidelines page.

## 4. Colour on a dark game UI

- Almost every surface is dark (launcher, server list, Discord dark theme): design **reversed-first**, then check
  the light version. Run `svg_audit.py --bg "#1e1f22"` (Discord dark) and `--bg "#313338"`.
- Keep the mark's luminance clearly above the background; avoid pure `#000` fills that vanish. Saturated neon on
  dark vibrates: desaturate the main fill ~10–15 % or add a calm neutral next to it.
- In-game text colours: if the brand colour must also appear in chat/scoreboards, it has to exist as a legal
  chat/MiniMessage colour (`§`-codes give 16 fixed colours; hex works on modern clients). Pick the brand palette
  so its core colour survives both — otherwise in-game branding drifts from the logo.
- Rank/tier palettes are a *system* (see `identity-system.md`): derive tiers from one hue family, don't add unrelated colours.

## 5. Names and wordmarks for servers/plugins

- Short, pronounceable names win (Hypixel-style compounds); check the name reads at 12–14 px in a bold sans.
- Mixed-case compounds (`SkyForge`) need the join designed, not just typed; avoid letter pairs that merge when
  tiny (rn/m, cl/d, I/l).
- Underscores, numbers-as-letters and decorative Unicode break search, copy-paste and fonts: keep the logo name
  plain ASCII, and provide the stylised version only as artwork.
- Provide a **tag form** (3–4 letters) for chat prefixes, tab lists and scoreboards: the logo should suggest it.

## 6. Delivery checklist (game / dev platforms)

Run once the direction is approved:

1. `export_variants.py … --web-icons` for the site (favicon, PWA).
2. `platform_icons.py logo-symbol.svg --bg <brand-dark> --circle` for server icon, Spigot/Modrinth/Hangar, Discord,
   avatar; `platform_icons.py logo-lockup.svg --presets github-social discord-banner` for wide assets.
3. Look at `server-icon.png` and the circle preview at actual size; fix, don't ship blindly.
4. If pixel-based: also deliver the 16×16 master as SVG (`crispEdges`) so it can be re-exported.
5. Mention in the guidelines: unaffiliated with Mojang/Microsoft, minimum sizes, dark-first colours, don't recolour tiers.
6. State unverified items: fonts assumed, platform size limits to re-check, no trademark search done.
