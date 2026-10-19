# Benchmark Scoring Rubric

Score each case per dimension as `pass / partial / fail`, citing the produced AST path or journey as evidence. Semantic equivalence passes: different tokens with identical user meaning score `pass`.

## Dimensions and weights

| Dimension | Weight | What earns pass |
|---|---|---|
| lifecycle semantics | 2 | create/info/remove/copy present and separated from mutation |
| vocabulary | 1 | canonical verbs per 19, no implementation-name leaks (22) |
| nesting depth | 1 | depth ≤ 4, no gratuitous levels (18) |
| permissions | 2 | capability-mapped nodes, no destructive grant to read roles (09/26) |
| contexts | 1 | player/console/automation explicit and safe (10/24) |
| completion | 1 | every argument completable from a real source, permission-filtered (11) |
| risk controls | 2 | destructive+ confirmed/scoped, system gated (23/34) |
| compatibility | 1 | changed paths dispositioned per 43/44 |
| journey outcomes | 2 | all case journeys achievable, including one failure path |

## Verdict

- `PASS`: no `fail`, at most one `partial`.
- `PASS WITH NOTES`: no `fail`, two or more `partial` with recorded reasons.
- `FAIL`: any `fail`, or any `forbidden` golden hit.

Record: `case, verdict, per-dimension evidence, forbidden check, journeys run`.
