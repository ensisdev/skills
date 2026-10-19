---
name: ensisdev-mc-scoreboard-engineering
description: Use when a Minecraft Java server scoreboard sidebar or TAB player-list is cluttered, inconsistent, hard to read, or needs new/revised copy, hierarchy, MiniMessage formatting, small caps, custom glyphs, resource-pack sprites, or placeholder wiring — or when the result needs an in-game-accurate preview before shipping.
license: MIT
---

# EnsisDev Mc Scoreboard Engineering

Teach design judgment while producing the artifact. Treat server identity, audience, version, and implementation surface as inputs; never impose one house template.

## Workflow

1. Extract server name, mode, language, audience, brand colors, Java/client version, plugin and text parser, resource-pack availability, and actual placeholders. Infer a restrained draft when details are missing and label assumptions. Ask only for facts needed for deployable config. Never invent working placeholders or claim a tag is supported without checking the chosen parser/version.
2. Choose what a player needs at a glance. Sidebar: identity, a small set of live facts, one action or location, and a quiet footer if useful. Start with 2–4 facts; allow more when the game mode genuinely demands them and the sidebar remains readable. TAB: identity, useful server status, player groups or columns when requested, and a short footer. Keep frequently updating data stable in position; avoid distracting loops and gratuitous counters.
3. Set hierarchy before decoration: one focal title, one accent color, neutral body text, contrast and deliberate blank space. Prefer short localized labels and consistent alignment. Avoid stars, repeated bars, excessive separators, rainbow gradients, emoji, and every feature at once. A symbol earns its place by conveying meaning or grouping. Offer a plain-text alternative if glyph support is uncertain.
4. Understand small caps as specific Unicode glyphs resembling reduced capitals, not a font-size setting. Use sparingly for short Latin headings only after checking coverage, width, baseline and game-scale legibility. Turkish `İ/ı/ğ/ş` and many letters lack matching small-cap glyphs; never silently transliterate names or Turkish words. Use ordinary text or a tested custom font. Read [design reasoning and supplied visual references](references/design.md) for examples. Inspect the bundled screenshots only when their visual evidence helps; do not infer TAB behavior or small-cap support from sidebar screenshots.
5. Create `design.json` following [preview format](references/preview-schema.md), including the `assumptions` array for every unverified fact. Run `python3 <skill-dir>/scripts/preview.py design.json -o preview.html --report report.json`. Inspect the HTML at wide and narrow viewport and revise crowding. This is an HTML approximation, not a Minecraft renderer: confirm critical glyphs, exact widths and plugin parsing in-game.
6. Apply the anchored 0–10 rubric in [design reasoning](references/design.md): usefulness, hierarchy, restraint, legibility and compatibility, 0–2 each. The script provides deterministic signals and a provisional score; add a human reason for any lost points. Make one focused revision if a dimension scores below 2. Do not chase a score by adding decorative content. Present final design, preview, score with evidence, and unverified integration points. Export plugin-specific config only after confirming its syntax.

## Implementation decisions

- Keep content separate from formatting and placeholders. Escape user-controlled text before MiniMessage parsing; never parse arbitrary placeholder output as trusted markup. Confirm refresh cadence and provider of each placeholder.
- Use `<shadow:#000000FF>` only when solid black shadow improves contrast and the target supports MiniMessage's shadow tag. Prefer the default or softer alpha if the full shadow is heavy. Literal MiniMessage is not universal across plugins or versions.
- Distinguish `<sprite:atlas:sprite>` from a custom bitmap font glyph. A sprite needs parser/client support and an atlas entry; a custom icon needs a distributed resource pack, font provider, mapping and fallback. Keep icons meaningful and few.
- Test unusual Unicode (emoji, private-use glyphs, small caps) in the exact client font. Browser fallback can succeed where Minecraft shows a box or a different width. Preserve critical meaning in ordinary text.
- Read [compatibility notes](references/compatibility.md) for tags, fonts, sprites, score values and third-party configuration. Consult current official documentation for version-specific behavior.

## Common mistakes

- Transliterating or small-capping Turkish letters (`İ/ı/ğ/ş/ü/ö/ç`) — most lack matching small-cap glyphs; use ordinary text or a tested custom font instead.
- Parsing placeholder output as trusted MiniMessage markup instead of escaping user-/placeholder-controlled text first.
- Using `<sprite:...>` or a custom bitmap glyph without confirming parser/client/atlas support — it renders as a box or wrong width on unsupported clients.
- Chasing a higher rubric score by adding decorative content instead of fixing the dimension that actually lost points.
- Treating the HTML preview as a Minecraft renderer — it approximates layout only; confirm exact glyph widths and plugin parsing in-game before shipping.

## Distribution

`agents/openai.yaml` is the ChatGPT/Codex/API/Atlas platform manifest (display name, icon, invocation prompt) for distributing this skill outside Claude; it is not read by Claude.

## Efficient use

Read `references/design.md` for design or critique; view `assets/reference-craftluna-1.png` and `assets/reference-craftluna-2.png` when analyzing the supplied visual style. Read `references/compatibility.md` only for implementation. Read `references/preview-schema.md` only to make preview input. Run the script without pasting its source or full HTML into context; inspect the small JSON report and rendered page. Use one representative preview and one revision unless a concrete defect remains.
