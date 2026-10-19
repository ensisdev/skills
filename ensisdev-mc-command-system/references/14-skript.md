# 14 — Skript Command Design

## Purpose

Adapts the command architecture to Skript-style commands while preserving the same UX principles.

## Separate command UX from implementation language

A Skript command is still a user API. The fact that the implementation is a Skript file does not justify weaker naming, completion or errors.

## Command components

Review:

- command name;
- aliases;
- permission;
- usage/help;
- arguments;
- player-only vs console;
- tab completion where supported by the project/runtime;
- parse errors;
- trigger behavior;
- external plugin command dependencies.

## Argument design

Prefer natural command paths such as:

```text
/warp create <name>
/warp delete <name>
/warp teleport <name>
```

over action names that expose script internals.

## Skript compatibility

Before changing a command, search all `.sk`, `.skrypt`, generated script folders and documentation for direct command calls.

Also search for commands embedded in:

- `make console execute command`;
- `execute player command`;
- GUI click actions;
- NPC/hologram actions;
- scheduled functions.

## Generated or dynamic commands

When the command set depends on runtime registrations, document the stable root and expose dynamic choices through completion/help where possible.

## Error behavior

A Skript command should distinguish parser failures from domain failures. Do not return an empty trigger or silent failure.
