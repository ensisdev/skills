# 16 — Anti-Patterns

## Purpose

Detects command designs that look organized in code but are poor for users.

### Verb explosion

Several verbs mean the same thing:

```text
make / new / create / generate
```

Choose one canonical semantic verb.

### CRUD leakage

Exposing database words such as `insert`, `update`, `row`, `persist` to users when the domain uses `create`, `set`, `save` or similar natural language.

### Deep nesting for no reason

Every implementation layer becomes a command token.

### Everything under `edit`

Putting lifecycle, inspection and destructive operations under `edit` merely for symmetry.

### Everything as a root command

Creating dozens of flat root subcommands even though the domain clearly has a resource namespace.

### Boolean ambiguity

A command where omission toggles state, `false` disables it, and `off` does something else.

### Property-per-root sprawl

Adding a new root command for every low-frequency field in a rich resource model.

### Completion afterthought

Command paths that technically parse but cannot be discovered or completed.

### Permission-by-class

Permission nodes generated from Java package/class structure rather than user capabilities.

### Compatibility break without audit

Renaming commands without searching scripts, GUIs, integrations and docs.

### Administrative leakage

Admin-only configuration operations accessible from a player-oriented command because both happen to touch the same domain object.

### Reference cloning

Copying FancyHolograms/FancyNpcs command names/nesting into a project whose domain does not match. Extract the principle, not the surface.
