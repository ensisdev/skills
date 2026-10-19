# ensisdev-mc-design — Minecraft Product Design System (v5)

Design skill for AI coding agents building Minecraft plugin interfaces.
Goal: recognizable, intentional, varied, **renderable** player-facing design that resists
AI design convergence.

---

## Quick routing — "I want to…" → read this

| I want to… | Read first | Then |
|---|---|---|
| Understand the philosophy & rules | `SKILL.md` | `rules/DESIGN_RULES.md` |
| Know what the platform can actually render | `SKILL.md` Step 0 | `references/RESOURCE_PACK_UI.md`, `references/BEDROCK_GEYSER.md` |
| Build a GUI menu | `rules/TACTICAL_GUIDE.md` §8–9 | `references/REFERENCE_LIBRARY.md`, `examples/EXAMPLES.md` EX-01..07 |
| Build a form / settings / confirmation | `references/MODERN_MC_FEATURES.md` §4 (Dialogs) | EX-02, EX-04, EX-23 |
| Write chat messages / errors (with the `[PluginName]` gradient prefix) | `SKILL.md` "Chat prefix standard", `rules/TACTICAL_GUIDE.md` §12, §18 | EXAMPLES EX-08..13, code patterns §18 |
| Design item names & lore | `rules/TACTICAL_GUIDE.md` §10–11 | EXAMPLES EX-14..17 |
| Use 1.21.x item components, shadow, display entities | `references/MODERN_MC_FEATURES.md` | `references/COMPATIBILITY.md` §6 |
| Custom GUI backgrounds / glyph icons / tooltip frames | `references/RESOURCE_PACK_UI.md` | — |
| Support Bedrock players | `references/BEDROCK_GEYSER.md` | — |
| Write Turkish copy / small caps / number formats | `references/TURKISH_COPY.md` | code patterns §19 |
| Add sound feedback | `references/SOUND_UX.md` | code patterns §15 |
| Pick a layout/composition | `rules/REFERENCE_PATTERNS.md` | `references/REFERENCE_LIBRARY.md` |
| Implement with MiniMessage/Adventure | `examples/MINIMESSAGE_CODE_PATTERNS.md` | `references/PAPERMc_REFERENCES.md` |
| Check version support risks | `references/COMPATIBILITY.md` | — |
| Avoid laggy UI patterns | `references/PERFORMANCE_NOTES.md` | code patterns §14 |
| Review a finished design | `qa/DESIGN_REVIEW_TEMPLATE.md` | `qa/DESIGN_VALIDATION.md` |
| Lint a design mechanically | `python -I tools/lint_messages.py <src>` | `rules/lint_rules.yaml`, `rules/ANTI_PATTERN_LINT.md` |
| Test that the skill still works | `qa/EVALS.md` | `tools/fixtures/` |
| See convergence caught & fixed | `qa/CASE_STUDIES.md` | — |
| Support toasts/signs/maps | STYLE_MATRIX rows | EXAMPLES EX-26..28 |

## Structure

```
SKILL.md                     core doctrine, platform check, loading map (~100 lines)
MANIFEST.json                version + content counts
README.md                    this routing file
rules/
  DESIGN_RULES.md            110 core normative rules   <- primary
  TACTICAL_GUIDE.md          detailed sections §1-§38 (moved out of SKILL.md in v5)
  DESIGN_RULES_300.md        per-surface expansion      <- appendix
  ANTI_PATTERN_LINT.md       human-readable lint
  lint_rules.yaml            machine-readable lint (incl. PREFIX-001..004)
  STYLE_MATRIX.md            surface -> UX goal matrix (26 surfaces)
  REFERENCE_PATTERNS.md      8 information-architecture families
references/
  REFERENCE_LIBRARY.md       46 composition references (9 families)
  MODERN_MC_FEATURES.md      1.20.5-1.21.x components, shadow, dialogs, displays
  RESOURCE_PACK_UI.md        glyph backgrounds, item models, tooltip styles, fallbacks
  BEDROCK_GEYSER.md          cross-play constraints, Floodgate forms
  TURKISH_COPY.md            Turkish typography, case, plurals, tone, glossary
  PAPERMc_REFERENCES.md      Paper/Adventure doc links
  SOUND_UX.md                auditory feedback layer
  COMPATIBILITY.md           client/server version risks
  PERFORMANCE_NOTES.md       refresh budgets, packet costs
examples/
  EXAMPLES.md                28 examples (GUIs drawn on real slot grids)
  MINIMESSAGE_CODE_PATTERNS.md  18 implementation patterns (incl. §18 prefix)
tools/
  lint_messages.py           stdlib linter for source/yaml message files
  fixtures/bad, fixtures/good  lint self-test inputs (bad must fail, good must pass)
qa/
  EVALS.md                   10 prompts with binary pass criteria
  DESIGN_VALIDATION.md       preflight + scoring checklist
  DESIGN_REVIEW_TEMPLATE.md  fillable review form
  CASE_STUDIES.md            bad->good redesigns with scores
  SELF_TEST_REPORT.md        end-to-end dry run of the skill
archive/                     retired v3 generated corpora (safe to delete; never load)
```

## Token budget guidance

- Every turn: `SKILL.md` only (~8 KB).
- Active designing: add `rules/DESIGN_RULES.md` + the one reference/example file that matches the task (~25 KB total).
- Detailed doctrine: open only the needed sections of `rules/TACTICAL_GUIDE.md`.
- Never bulk-load `archive/`.
