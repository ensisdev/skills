# 26 — Capability-Oriented Permission Architecture

## Purpose

Extension of `09-permissions-security.md`. Design permissions around what a user is allowed to do, not around the Java/Kotlin class tree or every parser branch. Read 09 first; come here when the project needs a designed inheritance tree or action-type permissions.

## Capability model

Typical capabilities:

```text
view
list
inspect
create
copy
edit
move
remove
bulk-edit
admin
reload
save
debug
```

Map commands to capabilities, then decide whether the project needs:

- one broad permission;
- resource-level permissions;
- operation-level permissions;
- action-type permissions.

## Permission granularity

Use finer permissions when:

- the operation is dangerous;
- different staff roles need different capabilities;
- an action can execute arbitrary commands;
- the project already has a documented permission surface.

Avoid permissions for every trivial property when that creates an unmaintainable matrix.

## Inheritance

Where the framework supports permission inheritance, design a coherent tree:

```text
plugin.resource.*
  plugin.resource.view
  plugin.resource.create
  plugin.resource.edit
  plugin.resource.remove
```

Do not create inheritance that accidentally grants destructive operations to a read-only role.

## Completion security

Completion must respect the same capability boundaries. Do not reveal protected resource names or action types through completion to unauthorized users.

## Migration

When command paths move, decide explicitly whether old permission nodes remain aliases, map to a new capability, or are deprecated.
