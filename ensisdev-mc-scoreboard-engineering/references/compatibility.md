# Compatibility and rendering

Check target server, client, plugin, parser and resource pack before exporting implementation strings. Scoreboard, TAB, Adventure components, legacy `§` codes and MiniMessage are distinct surfaces; a plugin may support only a subset.

## MiniMessage, when supported

PaperMC's [MiniMessage format](https://docs.papermc.io/adventure/minimessage/format/) documents color, `<font:key>`, `<shadow:#RRGGBBAA>` and `<sprite[:atlas]:sprite>` (sprite since Adventure 4.25.0). `<shadow:#000000FF>` means opaque black; it can overwhelm small glyphs. Close style scopes. Atlas/sprite identifiers name resources, not emoji. Verify parser version and exact atlas entry; preserve a textual fallback.

Minecraft's [24w44a notes](https://feedback.minecraft.net/hc/en-us/articles/31477609902477-Minecraft-Java-Edition-Snapshot-24w44a) describe text component `shadow_color`. Client support does not imply an older plugin parses a matching tag. Its [23w17a notes](https://feedback.minecraft.net/hc/en-us/articles/15245037698701-Minecraft-Java-Edition-Snapshot-23w17a) describe font providers and glyph width controls. Pack formats and components change by release; consult current release notes.

## Fonts and icons

An atlas sprite tag refers to an atlas sprite when supported. A bitmap font icon is a codepoint, often private-use, mapped by a resource pack font provider and selected via a font key. Record pack path, font key, codepoint, size/advance and plain fallback. Do not confuse Unicode small caps with custom glyphs. Browser emoji proves nothing about in-game support. Test missing-pack behavior, GUI scales and backgrounds.

## Content mechanics

Check real plugin line/length limits, score ordering, blank-line uniqueness, refresh interval, placeholder expansion and TAB sorting. Old server APIs may differ from component-aware ones. Give dynamic rows stable labels and bound large values. Do not parse untrusted player names or placeholder output as markup. When a dependency is unknown, supply a plain version and label styled output conditional.

## Common implementation surfaces

Verify the exact limits on the target before exporting; these are starting points, not guarantees.

| Surface | Practical limits | Notes |
|---|---|---|
| Vanilla sidebar | 15 lines; legacy ~40 chars/line | Order by score; blank lines need unique invisible content; one objective per display slot |
| FastBoard-style boards | ~15 lines practical; per-player dynamic | Update only changed lines to avoid flicker; recreating the board every tick flashes |
| TAB (e.g. NEZNAMY TAB) | Long header/footer; per-entry limits | Sorting runs through teams; animated headers cost bandwidth; keep header/footer short |
| Bossbar / action bar | One glanceable value | Not a paragraph surface; progress needs a matching max |

## Refresh and flicker budget

- Sidebar: 20-tick cadence is the default; per-tick rewrites cause flicker and wasted packets. Values that change rarely (coins, wins) must not trigger full redraws.
- Placeholder expansion (e.g. PlaceholderAPI) runs per player per refresh; per-tick expansion for many players is a known lag source. Prefer 20–40 tick cadence unless the value is a live timer.
- Timers and countdowns are the legitimate exception; keep them positionally stable so digits do not shift the layout.
- Header/footer animation faster than ~10 ticks distracts and costs bandwidth; prefer static text.

## Minimal export example

Export only after confirming the target's syntax. Generic shape for a lines-based board (adapt keys, placeholders and color codes to the plugin):

```yaml
# WAITING state: stable skeleton, two live facts
title: "PILLARS"
lines:
  - "Arena: {arena}"
  - "Oyuncu: {players}/{max}"
  - " "
  - "Mod: {mode}"
```

Each `{placeholder}` must name a verified provider and refresh cadence; record both in `implementation_notes` and any gap in `assumptions`.
