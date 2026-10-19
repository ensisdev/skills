# DESIGN VALIDATION

## Fast preflight

- Identify primary task.
- Identify top 3 information priorities.
- Name the composition family.
- Name the typography/casing treatment.
- Count decorative glyphs.
- Check small-caps usage.
- Check icon semantics.
- Compare against at least 3 nearby surfaces.
- Confirm at least 3 dimensions vary for an intentional redesign.
- Test long names, long numbers, and translated strings.
- Check empty/loading/success/error/disabled states where relevant.
- Ensure important state is not color-only.
- Ensure click/hover copy matches actual behavior.
- Record exceptions to rules.

## Anti-convergence score

Score 0–2 each: composition, typography, iconography, information architecture, spacing, interaction model, copy structure, state treatment. A deliberate redesign should normally score at least 10/16 against the nearest competing screen.

## Red flags

- sparkle/diamond/arrow glyph framing on title + every line
- same 9x6 glass-pane shell used without justification
- chat message missing the standard `[PluginName]` prefix, or a decorative separator after it
- every lore block is exactly three lines
- small caps used on every label
- color is the only state difference
- decorative icons with no semantic role
- redesign claims novelty while changing only color/glyph/title

## Exception record

When breaking a rule, state: **Rule ID → reason → affected surface → user benefit → review date**.

## Mechanical pass (run before the human checklist)

```
python -I tools/lint_messages.py <plugin source or resources dir>
```
Fix every ERROR. Review each WARN; either fix it or record the exception in the design review. Add `lint:ignore` in a comment on a line only for a justified false positive. Checks are heuristics: a clean run does not replace the checklist above.

