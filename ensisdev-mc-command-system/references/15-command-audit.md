# 15 — Command Audit

## Purpose

Final quality gate after design/implementation.

## A. Semantic consistency

- [ ] One canonical verb per meaning.
- [ ] Domain vocabulary matches project vocabulary.
- [ ] Similar operations use parallel grammar.
- [ ] `remove`, `clear`, `reset`, `delete` are not conflated.
- [ ] Spatial verbs make direction clear.

## B. Tree quality

- [ ] Root command is recognizable.
- [ ] Nesting depth is justified.
- [ ] High-frequency actions are not buried unnecessarily.
- [ ] Related operations are grouped.
- [ ] There are no duplicate command paths without a reason.

## C. Arguments and flags

- [ ] Arguments have domain-meaningful names.
- [ ] Types are validated early.
- [ ] Optional values have sensible defaults.
- [ ] Flags are reserved for modifiers/filters/options.
- [ ] Bulk operations are explicit.

## D. Discoverability

- [ ] Help covers the relevant command tree.
- [ ] Contextual help works where practical.
- [ ] Tab completion follows current context.
- [ ] Invalid input explains the expected form.

## E. Authorization

- [ ] Permissions map to meaningful capabilities.
- [ ] Dangerous operations are restricted.
- [ ] Completion respects permissions.
- [ ] Console restrictions are explicit.

## F. Compatibility

- [ ] Public command usage was searched.
- [ ] Internal/external calls were considered.
- [ ] Existing aliases were preserved or intentionally migrated.
- [ ] Permission compatibility was considered.

## G. Runtime validation

- [ ] Project builds/tests.
- [ ] Success path verified.
- [ ] Invalid argument path verified.
- [ ] Missing permission verified.
- [ ] Unknown resource verified.
- [ ] Player/console behavior verified.
- [ ] Completion verified.

## Audit result format

```text
COMMAND AUDIT: PASS | PASS WITH NOTES | FAIL

Blocking issues:
- ...

Non-blocking notes:
- ...

Compatibility notes:
- ...
```
