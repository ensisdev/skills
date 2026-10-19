# 12 — Compatibility and Migrations

## Purpose

Protects existing users when a command system is reorganized.

## Compatibility scan

Before renaming/removing a command, search for:

- documentation;
- README/website references;
- tests;
- internal command execution;
- GUI buttons/actions;
- NPC/hologram actions;
- Skript scripts;
- scheduled tasks/automation;
- examples/configuration;
- permissions;
- aliases.

## Canonical + compatibility alias

When safe, converge on:

```text
new canonical command
old command → alias/compatibility path
```

The compatibility command should not create a second divergent implementation.

## Deprecation

If an old command must remain:

1. mark it as compatibility/deprecated in code/docs where appropriate;
2. point users toward the canonical command;
3. keep behavior consistent;
4. remove it only according to a deliberate compatibility policy.

## Migration warnings

Do not spam users every time an old alias is used. Prefer documentation, a controlled warning or release-note migration guidance.

## Permission compatibility

Do not silently invalidate established permission nodes. If command paths move, decide whether permission inheritance/aliases can preserve access.

## Breaking-change threshold

A rename is more likely to be acceptable when the old command was:

- private/internal;
- undocumented;
- unused by integrated systems.

A rename is high risk when the command is:

- documented;
- used by automation;
- used by other plugins/scripts;
- commonly executed by players/admins.
