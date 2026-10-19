# 11 — Tab Completion

## Purpose

Defines completion behavior as a first-class command feature.

## Completion hierarchy

Completion should expose only values valid in the current context.

Example:

```text
/resource edit <cursor>
→ show existing resource names

/resource edit demo <cursor>
→ show only properties supported by demo

/resource action demo right_click add <cursor>
→ show registered action types
```

## Completion rules

1. Complete commands before values.
2. Complete valid domain resources rather than arbitrary text.
3. Filter as the user types.
4. Respect permissions.
5. Respect resource type/capability.
6. Avoid leaking secret or unauthorized resource names.
7. Keep large collections searchable/filterable.

## Dynamic completion

Generate choices from runtime registries when the project supports dynamic resources/action types.

## Completion for flags

Only suggest flags still applicable to the command and avoid repeatedly offering mutually exclusive flags.

## Spatial completion

World names, player names and known locations should complete from authoritative project/server sources.

## Completion is documentation

A good command can often explain itself through completion. Design completion alongside syntax rather than after implementation.
