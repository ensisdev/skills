# RESOURCE PACK UI — when vanilla is not enough

A vanilla chest GUI offers: a 9×N slot grid, item icons, item names, lore, and **one** title line. Everything else below requires a resource pack that the server delivers (and clients accept). Packs are a product decision: they cost download size, break on Bedrock, and can be declined. Design the vanilla version first; add the pack version as an enhancement.

---

## 1. Decision table

| You want… | Vanilla possible? | Needs pack | Cost / risk |
|---|---|---|---|
| Distinct button icons (lock, arrow, gear) | Partly (vanilla materials) | `item_model` / CMD | pack required; Bedrock needs Geyser mapping |
| Custom GUI background (shop panel art) | No | Font glyph in title | alignment fragility; Bedrock shows plain title |
| Text inside the GUI beyond title (headers, balance) | No | Font glyph or title text + offset | same |
| Right-aligned value / columns | No | Negative-space font + title | needs measured pixel widths |
| Custom tooltip frame | No | `tooltip_style` sprites | 1.21.2+ clients |
| Inline icons in chat/lore | Unicode only | Font provider or object components | fallback glyphs needed |
| Per-state button look (selected/locked) | Name/lore/glint | `item_model` states | fine, still needs fallback |

If the answer in your project is "no resource pack", **stop here** and use items, names, lore, glint, sound, and layout only.

---

## 2. Custom GUI background — how it works (conceptually)

The container **title** is rendered as text in a font. A pack can define a font whose glyphs are large images (e.g. a 176 px-wide panel). Setting the title to that glyph draws your image behind the slot icons, over the vanilla panel. Pieces:

1. **Bitmap font provider** — maps a private-use Unicode character to a PNG, with `height` and `ascent` controlling size and vertical offset.
2. **Space font provider** — `"type": "space"` with `advances` mapping characters to pixel widths (positive and **negative**). Negative advances move the cursor left, so the glyph can start at the GUI's left edge instead of the title's default inset.
3. **Title string** = `[negative-shift char(s)] + [panel glyph] + [shift back] + [optional real title text]`.
4. Slots stay at vanilla positions. Your art must be drawn to match the 18 px slot grid; the player inventory area is separate and also has fixed positions.

**Constraints and gotchas (test in client, do not trust arithmetic alone):**
- The title origin has a small inset from the GUI's left edge; the negative shift compensates for it. Value differs per GUI scale; measure in-game.
- Vertical placement uses `ascent`; some valid-looking combinations clip or fail to load — check the client log for font provider errors.
- Title text is drawn **under** items but **over** the vanilla background. Slot highlight and item tooltips still behave vanilla.
- Titles have a length limit (client-side truncation exists for long strings); keep the glyph string short.
- Changing GUI scale changes pixel alignment of everything *except* the grid — the panel scales with it; keep art on integer multiples.
- Dark-mode / HD packs a player installs on top can replace your glyph unless your namespace is unique. Use your own namespace for the font (`yourplugin:gui`).
- Glyph codepoints: use the Private Use Area; keep a table of assigned codepoints in the repo.

## 3. Layout rules when you control the art

1. Draw the panel on the real grid: columns at 18 px steps. Document each slot's purpose in a table next to the PNG.
2. Leave functional slots unobstructed visually: art should *label* regions (a "balance" plate above row 0), not hide that a slot is clickable.
3. Do not fake buttons with art over empty slots: an empty slot is not clickable. Put an invisible-model item (or a real icon) in every clickable slot.
4. Provide the same flow without the pack: same slots, plain titles. The pack changes appearance only.
5. Keep text out of art when it must be dynamic or localized; write it as real item names/lore.

## 4. Item icons for buttons

- Define models via `item_model` (1.21.2+) or custom-model-data selectors (1.21.4+/1.21.5 formats differ — see MODERN_MC_FEATURES.md).
- One base material per *button family* for fallback (e.g. `ARROW` for nav, `BARRIER` for close), so clients without the pack still see sensible icons.
- Icon states (normal / hover-less / disabled / selected) are **separate models**, not tints.
- Hide the vanilla tooltip noise (`tooltip_display`) so only your lore shows.

## 5. Glyph fonts for chat / lore / scoreboard

- Provide a plain-text fallback for each glyph (e.g. `$` for a coin glyph). Under MiniMessage use a resolver that swaps glyph vs. fallback based on "has pack" status.
- Glyph width must equal an integer pixel multiple; mismatched widths cause jitter on scoreboards.
- Glyphs in tablist/scoreboard: test with long names; glyph rows can push values out of view.
- Never put information **only** in a glyph.

## 6. Delivery and state

- Know whether the player accepted the pack (`PlayerResourcePackStatusEvent`). Store the status; select pack-or-plain UI per player.
- Required vs optional pack: required packs need a clear kick/decline message (design it: reason, size, retry command).
- Version the pack and hash it; re-send on change. Never ship UI that depends on a stale pack.

## 7. When NOT to use a pack for UI

- Bedrock cross-play is a priority (pack fonts do not render for Bedrock players).
- The UI is data-heavy and changes with translation (art bakes in language).
- A native Dialog would solve the same problem (forms/settings) with zero pack.
- The plugin is distributed to servers you do not control (you cannot guarantee a pack).

## 8. Checklist

- [ ] Vanilla variant designed first and works without a pack
- [ ] Every glyph has a text fallback; no info only in glyphs
- [ ] Slot map documented; every clickable slot holds a real item
- [ ] Alignment verified at GUI scales 1–4 and on at least one 1920×1080 and one smaller window
- [ ] Namespace unique; codepoint table maintained
- [ ] Pack status handled per player; declined state tested
- [ ] Bedrock behavior defined (see BEDROCK_GEYSER.md)
