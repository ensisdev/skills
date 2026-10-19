# EVALS — does the skill actually change the output?

Run each prompt in a fresh session with this skill available, then score the answer against its pass criteria. Record results in a copy of this table. A skill revision is an improvement only if the pass rate rises without new failures.

Scoring: ✔ pass · ✘ fail. Each criterion is binary and checkable from the answer alone.

---

## E1 — Shop GUI (platform reality)
**Prompt:** "Design the main shop menu for my Paper 1.21.4 survival server. No resource pack."
**Pass if:**
- [ ] States the platform assumption (vanilla, 9-column grid) before designing
- [ ] Draws the layout as slots (columns × rows), not text columns / right-aligned values
- [ ] Price is in item lore or name, balance in an item, not in the title
- [ ] No glass-pane border by default; whitespace grouping
- [ ] Mentions a fallback or limitation for any pack-only idea

## E2 — Chat messages (prefix standard)
**Prompt:** "Write the success, error and warning messages for a /market sell command."
**Pass if:**
- [ ] Every message starts with a gradient `[PluginName]` and exactly one space
- [ ] No `»`, `|`, `➜` after the prefix
- [ ] Bodies differ in shape (result-first vs problem+fix vs warning+action)
- [ ] The prefix is built once (helper), not repeated as a literal per message
- [ ] Player-supplied values go through `Placeholder.unparsed`

## E3 — Settings screen (right surface)
**Prompt:** "I need a settings screen with 3 toggles and a volume slider. Server is 1.21.8."
**Pass if:**
- [ ] Recommends a native Dialog (toggles + number range) over a chest GUI
- [ ] Provides a fallback for clients/servers below 1.21.6 or Bedrock
- [ ] Buttons are verbs naming effects, not OK/Cancel
- [ ] Validates input server-side

## E4 — Bedrock cross-play
**Prompt:** "We use Geyser. Design a confirm-purchase flow."
**Pass if:**
- [ ] Notes Bedrock limits (hotkeys, glyph fonts, hover)
- [ ] Gives a Floodgate `ModalForm` (or Dialog) path in addition to the chest GUI
- [ ] No action depends on shift-click, number keys or hover-only information

## E5 — Turkish small caps
**Prompt:** "Make Turkish small-caps labels for: Satış, Güvenlik, Pazar, Ayarlar, Görevler."
**Pass if:**
- [ ] Small-caps only `ᴘᴀᴢᴀʀ` and `ᴀʏᴀʀʟᴀʀ`
- [ ] Explains that `ç ğ ö ş ü` have no small-cap form and gives normal-case or a synonym for the rest
- [ ] Does not output a mixed word like `sᴀᴛış`

## E6 — Code review (lint)
**Prompt:** (give `tools/fixtures/bad/Messages.kt`) "Review this plugin message code."
**Pass if:**
- [ ] Finds missing prefix, string-concatenated MiniMessage, legacy `§`, separator after prefix, 4-stop gradient, paired glyph title, bad small caps, no-arg `toUpperCase()`, padEnd
- [ ] Fixes use `Chat.send`, `Placeholder.unparsed`, `Locale.ROOT`
- [ ] Does not "fix" by replacing one glyph with another

## E7 — Redesign without convergence
**Prompt:** "My plugin has 5 menus that all look the same (glass border, centered title, bottom nav). Redesign two of them."
**Pass if:**
- [ ] Changes ≥3 independent dimensions per redesigned menu and names them
- [ ] Compares against the other menus explicitly
- [ ] Keeps one shared identity (palette/typography roles)
- [ ] Includes empty/locked/error states

## E8 — Scope boundary (neighbor skills)
**Prompt:** "Create the Brigadier command tree and tab completion for /market."
**Pass if:**
- [ ] Defers command architecture to the command-system skill (or says it is out of scope)
- [ ] Only contributes command *copy* (usage, errors, help text) from this skill

## E9 — Hologram
**Prompt:** "Hologram above a shop chest showing owner and stock, Paper 1.21."
**Pass if:**
- [ ] Uses `TextDisplay` (not armor stands), 2 lines max, small view range
- [ ] No suffix generation on the owner's name (`Tezgah: Steve`, not `Steve'in`)
- [ ] No hover-only information

## E10 — Resource pack GUI
**Prompt:** "I want a custom GUI background with my logo for the shop."
**Pass if:**
- [ ] Explains the title-glyph + negative-space technique conceptually and warns about alignment testing
- [ ] Requires a vanilla fallback and a text fallback for glyphs
- [ ] Notes Bedrock does not show the pack glyph
- [ ] Every clickable slot still holds a real item

---

## Results log

| Date | Skill version | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 | E9 | E10 | Pass rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | v5.0.0 | | | | | | | | | | | |

## How to run E6 mechanically

```
python -I tools/lint_messages.py tools/fixtures/bad     # expect ERROR+WARN, exit 1
python -I tools/lint_messages.py tools/fixtures/good    # expect 0 findings, exit 0
```
