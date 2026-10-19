# 01 — Command Taxonomy

## Purpose

Defines the semantic vocabulary of commands. It answers **what kind of operation a command represents**. It does not define exact syntax, permissions, completion or scenario-specific behavior.

## Canonical operation families

### Lifecycle
Use when a durable resource enters/leaves/duplicates existence.

- `create` — create a new resource.
- `remove` — permanently remove a resource.
- `copy` — duplicate an existing resource under a new identity.
- `reset` — restore a known default state; use only when reset semantics are real.

Avoid synonyms such as `make`, `new`, `delete`, `destroy`, `duplicate` unless compatibility or project vocabulary requires them.

### Inspection

- `list` — enumerate resources.
- `info` — inspect one resource.
- `nearby` — spatially scoped enumeration.
- `find` / `search` — semantic lookup when `list` cannot express the search naturally.
- `status` — runtime/system state rather than resource description.

### Mutation

- `set` — replace one value.
- `add` — append a member to a collection.
- `remove` — remove a member or resource; disambiguate by context.
- `clear` — empty an entire collection.
- `edit` — namespace for multiple property-oriented operations when grouping improves usability.

### Spatial operations

- `move_here` / project-specific equivalent — move the target to the executor's current location.
- `move_to` — move the target to a specified location.
- `teleport` — teleport the executor or target; grammar must make the direction unambiguous.
- `rotate` — change orientation.
- `center` — normalize alignment around a meaningful spatial reference.

### Actions and triggers

- `action` — manipulate an executable action sequence.
- `trigger` — identify the event condition driving actions when needed.
- `add`, `insert_before`, `insert_after`, `set`, `remove`, `move_up`, `move_down`, `clear`, `list` — sequence operations.

### System administration

- `reload` — re-read configuration/runtime definitions; must not silently rebuild unrelated state.
- `save` — persist runtime state when manual persistence is supported.
- `version` — show version/update information.
- `debug` — enable/show diagnostic information; keep diagnostic commands separate from gameplay mutations.
- `convert` — import/transform data from an external format or legacy plugin.

## Selection rules

1. Prefer semantic verbs over implementation verbs.
2. Use the same canonical verb everywhere a meaning is identical.
3. Use a different verb only when the user-visible operation is materially different.
4. Do not add a subcommand solely because a similarly named Java method exists.
5. If a command is a pure property mutation and grouping it under `edit` substantially reduces root-level clutter, use an edit namespace.
6. If a property is a primary user workflow (for example a shop price), a direct property command may be clearer than deep nesting.

## Ambiguous vocabulary to avoid by default

- `manage`
- `modify`
- `operate`
- `process`
- `do`
- `execute` when an actual user-facing action verb exists

These are acceptable only when the project has a precise established meaning.
