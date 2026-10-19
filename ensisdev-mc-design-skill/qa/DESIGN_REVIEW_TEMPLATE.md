# DESIGN REVIEW TEMPLATE

Fill one per player-facing surface before delivery. Copy this file into the
plugin repo under `docs/design-reviews/<surface>-<date>.md`.

---

```markdown
# Design Review — <surface name> (<date>)

## 1. Task definition
- Primary player task: <browse / compare / configure / claim / confirm …>
- Top 3 information priorities: 1) … 2) … 3) …
- Trigger & frequency: <command/menu entry; high/low frequency>

## 2. Composition
- Family chosen (grid/dashboard/rail/detail/wizard/comparison/console): 
- Reference IDs used (2–4, different families): REF-__, REF-__
  - Borrowed conceptually: 
  - Deliberately changed: 
  - Plugin-specific constraint that shaped it: 

## 3. Typography plan
- Title treatment: <small-cap label + normal title / plain bold / …>
- Casing rules per element class: titles=…, labels=…, values=…, body=…
- Small-caps usage justified (short labels only?): 

## 4. Iconography
- Icons and their semantic role (object/action/state/category): 
- Decorative glyph count per cluster (0–2): 

## 5. Color semantics
- Roles used from palette: brand/success/warning/danger/muted/value
- Any new color introduced? Justify or remove.

## 6. States covered
[ ] default [ ] hover-equivalent [ ] selected [ ] disabled
[ ] empty (+next action copy) [ ] loading [ ] success [ ] error (+recovery)
[ ] locked (+requirement)

## 7. Resilience
- Longest realistic string tested (16-char names? big numbers?): 
- Translation-safe layout (no English-width assumptions)? 
- Hover-only information? (must be none)
- Dynamic values via unparsed placeholders?

## 8. Sound (if applicable)
- Cues by role (confirm/error/open/close): 
- Rate limits respected?

## 9. Anti-convergence score vs nearest neighbor screen
| Dimension | Same as neighbor? | Varied how |
|---|---|---|
| composition | | |
| typography | | |
| iconography | | |
| information architecture | | |
| spacing | | |
| interaction model | | |
| copy structure | | |
| state treatment | | |
Score: __ varied of 16 → target ≥10 for deliberate redesigns; ≥3 dimensions must differ.

## 10. Lint pass (rules/ANTI_PATTERN_LINT.md)
Triggered IDs (should be none at ERROR level): 

## 11. Exceptions
Rule ID → reason → affected surface → user benefit → review date:

## Verdict: SHIP / REVISE (what exactly changes first?)
```
