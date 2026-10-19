# 09 — Permissions and Security

## Purpose

Defines authorization boundaries for commands. This is the security baseline; `26-permission-architecture.md` extends it with capability-tree design for granular staff hierarchies. Read this file first.

## Permission design

Permission nodes should map to meaningful capabilities rather than implementation classes.

Good conceptual model:

```text
plugin.command.root
plugin.command.resource.create
plugin.command.resource.remove
plugin.command.resource.edit
plugin.command.resource.action.add
```

## Granularity rule

Use granular permissions when:

- operations have materially different risk;
- different staff roles legitimately need different capabilities;
- bulk/destructive actions need stronger access.

Use broader inherited permissions when fine granularity would create unmanageable permission sprawl.

## Player-facing commands

Gameplay commands should not automatically inherit administrative permissions. A player should have the smallest capability needed for the feature.

## Console

Decide explicitly whether a command supports console. Resource operations requiring a player location must either:

- be player-only;
- accept an explicit location alternative;
- or have a documented console behavior.

Never silently use a fake/default location.

## Dangerous actions

Treat these with special care:

- bulk deletion;
- economy manipulation;
- permission changes;
- arbitrary console execution;
- server shutdown/reload;
- data conversion/migration.

These should have explicit authorization and, where needed, confirmation.

## Dynamic action permissions

For plugin systems with user-defined action types, permission resolution may need to include the action type. Use this only when the action semantics justify it.
