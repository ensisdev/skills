# MODERN MINECRAFT FEATURES — what 1.20.5 → 1.21.x changed for UI design

Decision aid, not an API guarantee. Version rows were checked against Paper/Adventure documentation and Mojang snapshot notes in October 2026 (sources in `PAPERMc_REFERENCES.md` §10). Rows still marked **(unconfirmed)** come from memory only; check them before relying on them. If the project's minimum version is lower than a feature's version, treat the feature as an enhancement with a fallback (see COMPATIBILITY.md §4).

---

## 1. Timeline

| Version | Change | Design impact |
|---|---|---|
| 1.19.4 | Display entities (`TextDisplay`, `ItemDisplay`, `BlockDisplay`) | Holograms without armor stands; real background, billboard, line width, alignment |
| 1.20.3 | Scoreboard `NumberFormat` (blank / fixed / styled), introduced in snapshot 23w46a; Paper has an objective number-format API | Scoreboard right-hand red numbers can be hidden or replaced with real values |
| 1.20.5 | Data components replace item NBT: `item_name`, `custom_name`, `lore`, `custom_model_data`, `enchantment_glint_override`, `max_stack_size` … | Use `item_name` for plugin-defined names (not italic by default, not anvil-renamable); `custom_name` is the player-renameable layer |
| 1.21.2 | `item_model` and `tooltip_style` components | Swap an item's model without custom-model-data ranges; give GUI items their own tooltip frame |
| 1.21.4 | Item model definition files (`assets/<ns>/items/*.json`); text `shadow_color` style attribute (Adventure 4.18, released 2024-12-22, added support) | Conditional/select models; shadow control for text |
| 1.21.5 | `custom_model_data` becomes floats/flags/strings/colors; `tooltip_display` component (hide whole tooltip or chosen components); text components use SNBT with `click_event` / `hover_event` objects | One item can carry several model switches; precise tooltip control instead of legacy item flags |
| 1.21.6 | Native **Dialog** screens (`/dialog`, server-sent) | Real forms: text inputs, toggles, sliders, option pickers, buttons |
| 1.21.7/1.21.8+ | Paper Dialog API (`io.papermc.paper.dialog.Dialog`, annotated `@Experimental`; present in the 1.21.8 Javadoc, 1.21.7 **(unconfirmed)**) | Use via API; expect signature changes; keys on dialogs are deprecated for removal, use registry lookups |
| 1.21.9 | Object text components (atlas sprites, player heads inside text). Adventure serialization + MiniMessage `<sprite>` / `<head>` tags arrived in **Adventure 4.25.0** (2026-04-16) | Inline icons without a custom font; player heads render 8×8 and the hat layer can vanish at low chat opacity |

Paper also provides a `MenuType` builder API for typed custom containers **(unconfirmed exact version)**; and Adventure `Component` titles for `createInventory`.

---

## 2. Item components for design (replace NBT/flags thinking)

- **Names:** `item_name` = the plugin's authoritative name. `custom_name` = player rename; do not fight it. Italic is default only for `custom_name`; if a name looks italic, you set the wrong component or forgot `decoration(ITALIC, false)` on legacy paths.
- **Tooltip control:** prefer `tooltip_display` (1.21.5+) over hiding via flags. Hide attribute/enchant/“Unbreakable” noise on GUI buttons so lore is the only text. Hidden info must not be the only copy of that info.
- **Tooltip frame:** `tooltip_style` → resource pack sprites `textures/gui/sprites/tooltip/<name>_background.png` and `<name>_frame.png`. Use for tiers/rarity/currency items; one style per *meaning*, not per whim.
- **Models:** `item_model` for visual identity of GUI buttons (arrow, lock, gear). Avoids reusing `PAPER` + CMD ranges everywhere. Requires a resource pack; vanilla fallback = a sensible vanilla material.
- **Glint:** `enchantment_glint_override` is a legit *state* signal (selected/active) — only if one glint = one meaning in the whole plugin.
- **Stack size / max damage:** GUI buttons should be non-stackable-looking (`max_stack_size` 1) so counts never leak into the icon corner unintentionally.

## 3. MiniMessage / Adventure additions worth designing with

- `<shadow:color:alpha>` (alpha float 0–1, default 0.25; `#RRGGBBAA` hex also accepted) and `<!shadow>` (= `<shadow:#00000000>`) — Adventure ≥ 4.18, client ≥ 1.21.4. Soften or recolor the text shadow; helps contrast of light text on bright backgrounds.
- `<sprite[:atlas]:sprite>` and `<head:name|uuid|texture[:outer_layer]>` — object components, Adventure ≥ 4.25.0, client ≥ 1.21.9. Example: `<sprite:item/emerald>`. Always add a text fallback for older clients and Bedrock.
- `<font:namespace:name>` — switch to a pack font for glyph icons; **always** pair with a plain-text fallback for clients without the pack and for Bedrock.
- `<lang:key>` / translatable components — let the client translate vanilla names (`block.minecraft.diamond`) so item names localize for free.
- `<click:…>` / `<hover:…>` — in 1.21.5+ serialization is via `click_event` / `hover_event`; use Adventure builders, do not hand-write JSON.
- Placeholders: `Placeholder.unparsed` for player text, `Placeholder.component` for trusted components, `TagResolver` for repeating tags. Never format player text into the MiniMessage *string*.

## 4. Native Dialogs (1.21.6+) — the biggest UX shift

A Dialog is a client-rendered screen: title, body (plain messages, items), **inputs**, and **buttons**, optionally with a "pause game" flag and escape handling.

**Dialog types:** `notice` (one button), `confirmation` (yes/no), `multi_action` (N buttons in columns), `server_links`, `dialog_list` (submenu of dialogs).
**Input controls:** text field, boolean toggle, number range slider, single-option selector.
**Button actions:** run command, open dialog, custom payload to server, open URL, copy to clipboard, suggest command, change page (**unconfirmed** exact action ids per version; check the Javadoc of `io.papermc.paper.registry.data.dialog.action` for your build).

**Use a Dialog instead of a chest GUI when:**
- the task is a **form** (create listing: price + duration + visibility),
- the task is a **settings** screen with toggles/sliders,
- the task is a **confirmation with consequences** (long sentence + 2 buttons),
- you need **free text/number input** (replaces anvil/sign/chat-prompt hacks).

**Keep the chest GUI when:** the player browses/compares *items*, drags items, or needs a live slot grid.

**Dialog design rules:**
1. Title ≤ ~30 characters; the consequence sentence goes in the body, not the title.
2. Buttons are verbs naming the effect ("Close stall & cancel 2 listings"), never OK/Cancel.
3. Destructive and safe buttons must differ in label *and* position; do not rely on color alone.
4. Provide the same flow for pre-1.21.6 clients (anvil/sign/chat prompt or chest) — Dialog is an enhancement, not the only path, unless the project minimum is ≥ 1.21.6.
5. Validate every input server-side; dialog input is client-supplied.
6. Do not open a dialog from a tight loop or on every join; it takes over the screen.

## 5. Display entities (holograms, world UI)

- `TextDisplay`: `background` color (ARGB), `see_through`, `line_width`, `alignment`, `text_opacity`, `billboard` (fixed / vertical / horizontal / center), `view_range`, `shadow`.
- Prefer one multi-line `TextDisplay` over stacked armor stands; fewer entities, consistent line spacing.
- Set `view_range` small (a few blocks to ~16) — holograms are glanceable, not skybox signs.
- `ItemDisplay` is a legitimate "icon in the world" for shops/quests (rotate slowly or not at all; constant spin is noise).
- Interaction: pair with an `Interaction` entity for click targets; the display itself is not clickable.
- Folia: schedule display updates on the region/entity scheduler of the owning location, not the global scheduler.

## 6. Scoreboard / tablist notes

- Hide red numbers with a blank `NumberFormat` when the number is meaningless; use a styled format when the number *is* the value (balance, kills).
- Sidebar title is one line; lines are limited by screen height and client width — design for ~12 rows × ~28 visible characters.
- Updates: batch changes per tick; avoid re-sending identical lines (see PERFORMANCE_NOTES.md).
- Tablist header/footer accept Components; use for navigation hints and identity, not ASCII art.

## 7. Defaults to adopt in new plugins (when min version ≥ 1.21.5)

1. `item_name` for plugin item names; `tooltip_display` to hide noise.
2. Dialog for forms/confirmations, chest GUI for item browsing.
3. `TextDisplay` for holograms.
4. Pack fonts/sprites for icons *only if* a resource pack is guaranteed; otherwise ASCII-safe semantic icons.
5. Adventure builders everywhere; no raw JSON, no legacy `§` strings.
