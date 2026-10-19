# BEDROCK / GEYSER / FLOODGATE — design constraints for cross-play

Applies when the server runs Geyser (Bedrock → Java translation), usually with Floodgate (Bedrock accounts without Java auth). Behavior varies by Geyser version and Bedrock platform (mobile/console/PC) — **verify against current Geyser docs and test on a real Bedrock client.** This file lists design risks, not guarantees.

---

## 1. What changes for Bedrock players

| Surface | Risk | Design response |
|---|---|---|
| Chest GUIs | Container titles may be truncated; lore wraps differently; hotkeys and drag gestures differ | Short titles (put key info in item names), no multi-step drag interactions |
| Click types | No reliable middle click, number-key swap, drop-key, double-click on touch/console | Primary action = left click; secondary = right click **and** an on-screen alternative; never gate essentials on hotkeys |
| Resource-pack fonts / glyph backgrounds | Java packs do not apply; custom glyphs show as boxes or missing | Plain-title fallback; never put information only in a glyph |
| `item_model` / CMD icons | Need Geyser custom item mappings (extra work) | Pick a sensible base material as fallback |
| Native Dialogs | Support depends on Geyser version | Detect and fall back; or use Floodgate forms |
| Small-caps / symbol Unicode | Bedrock font has different coverage; some glyphs missing or different width | ASCII-safe alternatives for critical info; test small caps (`ᴍᴀʀᴋᴇᴛ`) on Bedrock |
| Chat hover/click | Hover is unavailable on touch; click support is limited | No hover-only information; commands shown in plain text |
| Scoreboard / tablist | Different line limits and fonts | Fewer, shorter lines; avoid column alignment by spaces |
| Action bar / titles | Generally work, but timing differs | Keep short; do not depend on exact fade timing |
| Boss bars | Work but style options differ | Do not encode meaning in bar *style/overlay* alone |
| Display entities (holograms) | Rendering is generally supported but details can differ | Test view range and background |

## 2. Floodgate Forms — Bedrock-native UI

Floodgate exposes Bedrock **Forms**: `SimpleForm` (title + content + buttons, optional images), `ModalForm` (two-button confirm), `CustomForm` (toggle, slider, dropdown, step slider, input, label).

Use Forms for Bedrock where a Java player would get a Dialog (1.21.6+) or a form-like GUI:

| Task | Java 1.21.6+ | Java older | Bedrock |
|---|---|---|---|
| Confirm with consequences | Dialog `confirmation` | chest confirm GUI | `ModalForm` |
| Settings with toggles | Dialog `multi_action` + inputs | chest GUI with state items | `CustomForm` |
| Pick one option from a list | Dialog `single_option` / multi_action | paginated chest | `SimpleForm` |
| Item browsing/grids | Chest GUI | Chest GUI | Chest GUI (via Geyser) or `SimpleForm` list with images |

Rules:
1. Same wording and same outcomes across platforms; only the container changes.
2. Detect the player type once (Floodgate API `isFloodgatePlayer`) and route to the matching presenter; keep presenters behind one interface (`ConfirmView`, `SettingsView`).
3. Forms are modal and blocking; do not open them in loops or from passive events.
4. Validate form responses server-side exactly like command input.

## 3. Text and layout

- Assume narrower usable width on mobile; wrap earlier.
- Do not align columns with spaces — proportional fonts differ per platform.
- Keep lore lines short (about 30–35 characters) and avoid dependence on line breaks inside a sentence.
- Colors are generally supported; gradients degrade to nearest color on some paths. Use single-color fallbacks.
- Emoji/ornamental symbols: assume risk; keep meaning in words.

## 4. Testing matrix (minimum)

| Check | Java vanilla | Java + pack | Bedrock mobile | Bedrock console/PC |
|---|---|---|---|---|
| GUI title readable | ✔ | ✔ | ✔ | ✔ |
| All essential actions reachable by left/right click | ✔ | ✔ | ✔ | ✔ |
| No info only in glyph/hover | ✔ | ✔ | ✔ | ✔ |
| Small caps / symbols render | ✔ | ✔ | ✔ | ✔ |
| Dialog or form fallback works | ✔ | ✔ | ✔ | ✔ |

## 5. Anti-patterns

- Glyph-art GUI backgrounds with no plain fallback.
- "Shift-click to confirm" as the only confirm path.
- Hover tooltips carrying the only copy of a price or rule.
- Decorative Unicode borders on titles (truncation turns them into broken fragments).
- Dialog-only flows without a fallback when Bedrock players are present.
