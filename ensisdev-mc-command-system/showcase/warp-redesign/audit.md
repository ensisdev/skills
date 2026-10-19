# Showcase audit (Phase 14)

```text
COMMAND ARCHITECTURE AUDIT
Result: PASS WITH NOTES

Observed:
- E-001..E-009 (see evidence-ledger.md)

Inferred:
- E-010 Folia risk, E-011 grief risk

Proposed:
- E-012 alias preservation, E-013 admin root (implemented in new-ast*.json)

Blocking issues:
- none

Non-blocking notes:
- N-1: per-warp variable pricing (arena free vs others $50) is data-driven;
  completion shows cost per entry but the AST models one cost shape.
  Accepted: snapshot providers carry cost metadata; revisit if pricing rules grow.
- N-2: console travel needs explicit target (warp go is player-only);
  accepted: console uses warpadmin paths; documented in help.

Compatibility:
- all four documented paths dispositioned (see migration.md)

Journey tests:
- J-1 discovery: /warp list renders paginated clickable list — pass
- J-2 travel: go (confirm names $50) → arrive — pass
- J-3 invalid: unknown warp → domain error with suggestion — pass
- J-4 permission: player attempts warpadmin delete → generic denial — pass
- J-5 destructive: delete → named confirm → audit log — pass
- J-6 compat: /warp spawn and /warplist resolve — pass
```

Tool gates: `ast_lint` 0 errors on both ASTs; `collision_check` 0 errors.
