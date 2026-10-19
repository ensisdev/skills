---
name: ensisdev-mc-design-skill
description: Use when creating or reviewing player-facing Minecraft plugin surfaces — GUIs, chat messages, item names and lore, scoreboards, tablists, holograms, bossbars, command UX, dialogs, onboarding, notifications, shops, profiles, settings — or when a design looks generic, templated, or like every other AI-generated Minecraft UI.
license: MIT
---

# ensisdev-mc-design v5 — Minecraft Product Design System

## Mission

Create Minecraft plugins whose player-facing experience is **recognizable, intentional, varied, readable, implementation-aware, and resistant to AI design convergence**. Applies to every visible or readable surface: inventory menus, chat, item names/lore, action bars, bossbars, scoreboards, tablists, holograms, dialogs, books, signs, toasts, notifications, onboarding, shops, profiles, settings, quests, mailboxes.

Treat the design layer as a product system, not decoration added after coding.

## Step 0 — Platform reality check (do this BEFORE designing)

Most bad Minecraft designs are impossible designs. Before any layout, answer:

1. **Target versions** — server (Paper/Spigot/Folia) and minimum client. Read `references/MODERN_MC_FEATURES.md`.
2. **Resource pack?** A vanilla chest GUI is a 9-column slot grid plus a single title line. It has no text columns, no right-aligned values, no buttons, no panels. Anything beyond items, names, lore and one title requires a resource pack (`references/RESOURCE_PACK_UI.md`). **Never mock up a layout the platform cannot render.** Draw GUIs as slot grids (see `examples/EXAMPLES.md`).
3. **Bedrock players?** Geyser/Floodgate changes fonts, hotkeys and dialogs. Read `references/BEDROCK_GEYSER.md`.
4. **Right surface?** Item grids → chest GUI. Forms, settings, confirmations, text input → native Dialog (1.21.6+) or anvil/sign fallback. Passive info → action bar / bossbar / toast. Choose the surface from the task, not habit.

## Loading map (retrieve only what the task needs)

| Task | Load |
|---|---|
| Any non-trivial surface | this file + `rules/DESIGN_RULES.md` |
| Choosing layout/composition | `rules/REFERENCE_PATTERNS.md`, `references/REFERENCE_LIBRARY.md`, `rules/STYLE_MATRIX.md` |
| Concrete mockups to adapt | `examples/EXAMPLES.md` |
| Implementation (Adventure/MiniMessage) | `examples/MINIMESSAGE_CODE_PATTERNS.md`, `references/PAPERMc_REFERENCES.md` |
| 1.21.x item components, shadow, dialogs, display entities | `references/MODERN_MC_FEATURES.md` |
| Custom GUI backgrounds, glyph fonts, tooltip styles | `references/RESOURCE_PACK_UI.md` |
| Bedrock / cross-play | `references/BEDROCK_GEYSER.md` |
| Turkish copy, small caps with ç/ğ/ö/ş/ü, İ/I, plurals, number formats | `references/TURKISH_COPY.md` |
| Version/glyph risk, refresh cost, sound | `references/COMPATIBILITY.md`, `references/PERFORMANCE_NOTES.md`, `references/SOUND_UX.md` |
| Detailed per-surface doctrine (§1–§38: GUI, titles, lore, chat, bossbar, scoreboard, tablist, hologram, color, typography, icons, i18n, a11y, refactor workflow) | `rules/TACTICAL_GUIDE.md` — read only the matching sections |
| Unusual surface variants | `rules/DESIGN_RULES_300.md` (appendix; mostly per-surface restatements) |
| Review / validation | `qa/DESIGN_VALIDATION.md`, `qa/DESIGN_REVIEW_TEMPLATE.md`, `rules/lint_rules.yaml`, `rules/ANTI_PATTERN_LINT.md`; run `python -I tools/lint_messages.py <src>` for the mechanical pass |
| Check the skill itself | `qa/EVALS.md` |
| Worked before/after | `qa/CASE_STUDIES.md` |

`README.md` has the task-based routing table. `archive/` holds retired v3 generated corpora — never load it.

## Neighbor skills (scope boundaries)

| Need | Use | This skill's part |
|---|---|---|
| Scoreboard sidebar / TAB layout, placeholders, MiniMessage sprites | `ensisdev-mc-scoreboard-engineering` | general rules (hierarchy, glyph budget, no hover-only info) |
| Command tree, Brigadier, tab completion, permissions | `ensisdev-mc-command-system` | command *copy*: usage, errors, help wording, onboarding |
| Block-display scenes, set pieces | `ensisdev-mc-blockdisplays` | text/hologram copy inside a scene |
| Generic web/app UI | not this skill | — |

If a request is mostly one of the left-hand needs, load that skill first and use this one only for the player-facing wording and visual-language checks.

## Anti-convergence principles

1. Replacing one decorative glyph with another is not redesign.
2. Recoloring the same layout is not redesign.
3. Changing only the title wording is not redesign.
4. A component may repeat only when it earns repetition (usability or brand consistency).
5. An intentional redesign changes **≥3 independent dimensions**: composition, typography, hierarchy, interaction model, iconography, spacing, copy structure, density, navigation.
6. Small caps are a typographic tool, not a universal heading style.
7. Icons encode meaning (object, action, state, category) or they are removed.
8. Decorative Unicode has a budget (0–2 per visual cluster).
9. Semantic structure over visual noise; important info must survive with all decoration removed.
10. Not every GUI is a centered 9x6 chest with glass-pane borders and a bottom nav bar.
11. Chat messages carry the plugin's standard gradient `[PluginName]` prefix; variety lives in the message *body* (result-first, recovery, etc.), never in the prefix.
12. Not every lore is symbol + label ×3.
13. One coherent visual language, multiple compositions: **same identity, different compositions.**
14. When the player's task changes, the information architecture may change.
15. When reviewing against nearby screens, state explicitly what was varied.

## Design decision order

**platform constraints → player goal → information hierarchy → interaction model → composition → typography → iconography → color semantics → microcopy → decorative polish.**
Never start with "which symbol should I use?".

## Diversity budget

Compare each new surface with the plugin's 3–6 nearest surfaces across: layout family · density · title treatment · casing · icon strategy · frame strategy · navigation placement · primary/secondary action placement · empty-state treatment · success/error language · lore/message shape · spacing rhythm. Do not repeat all at once. A family resemblance is good; a clone is not.

## Condensed policies

- **Small caps** — short labels, status tags, category markers only. Not long text, player names, numbers, error diagnostics, or every menu line. Do not fake with random lookalike Unicode unless the target font is known to render it (check Bedrock: `references/BEDROCK_GEYSER.md`).
- **Icons** — answer "what object/action/state/category?" or delete. Prefer item/resource-pack sprites over decorative stars/arrows/diamonds.
- **Messages** — every chat message starts with the plugin prefix: a gradient `[PluginName]` in square brackets, one space, then the body (see "Chat prefix standard" below). Vary the body architecture by intent: result-first, action-first, context-first, state-first, progress, warning block, guided recovery, receipt. No decorative glyph or `»` after the prefix.
- **Lore** — scannable structures: identity→effect→requirements→action; summary→comparison→action; state→progress→next step; flavor→mechanics; ownership→controls. Avoid the universal 3-line recipe.
- **GUI** — choose a composition family deliberately (grid, dashboard, split-pane, carousel, category wall, detail view, wizard, matrix, timeline, collection board, minimal utility, hybrid) **within the real slot grid**. Never claim a layout is possible if the platform/API cannot render it.
- **References** — design prompts, not templates. Combine 2–4 from different families; record IDs, what was borrowed, what changed, what plugin constraint shaped the result.

## Chat prefix standard (project decision)

- Form: `<gradient:#from:#to>[PluginName]</gradient>` + one space + body. Brackets are part of the gradient.
- One prefix per plugin, identical in every chat message (success, error, info, broadcast). It is the plugin's identity mark; the body carries the hierarchy.
- Gradient: 2 stops (3 max), brand-derived, readable on dark and light chat backgrounds; define a single-color fallback for clients/paths without hex support (COMPATIBILITY §4 rule 002).
- No separator glyph after it (`»`, `>>`, `|`, `➜`) and no decoration inside it. Do not put the prefix on action bar, bossbar, titles, GUI text, lore or scoreboard — those have their own identity mechanics.
- Severity is conveyed by the body (wording, `✓`/`!` icon, body color), not by changing the prefix.
- Build it once (see `examples/MINIMESSAGE_CODE_PATTERNS.md` §18), never hand-type it per message.

## Required design review before delivery

1. Primary task · 2. information hierarchy · 3. composition family · 4. typography hierarchy · 5. icon strategy · 6. small-caps check · 7. glyph count · 8. compare with nearby screens · 9. anti-convergence checks · 10. dynamic text localizes/resizes safely · 11. click/hover affordances understandable without decoration · 12. empty/loading/success/error/unavailable states · 13. long names and large values · 14. **mockup is renderable on the declared platform (vanilla vs resource pack vs Bedrock)** · 15. record intentional rule exceptions.

## Output expectation for a coding agent

Return implementation-ready decisions, not style adjectives: target platform assumptions, selected visual direction, component structure (as a slot grid for GUIs), typography/casing plan, icon semantics, message/lore structure, interaction states, anti-convergence review. Then implement with the project's existing API and conventions.

## Safety and compatibility guardrails

Do not invent unsupported API behavior. Do not use fragile Unicode just to satisfy a visual brief. Do not rely on invisible formatting that breaks copy/paste or localization. Escape/sanitize all player-supplied text (use `Placeholder.unparsed`, never string-concatenate into MiniMessage). Do not hide important state exclusively behind hover. No color-only distinctions. Prefer explicit labels, item names, action verbs and status words. Do not make essential actions depend on keys Bedrock/touch players lack (number-key swap, drop, middle click).
