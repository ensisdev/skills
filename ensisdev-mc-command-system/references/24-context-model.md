# 24 — Executor Context Model

## Purpose

Defines how the same semantic operation behaves across actors and invocation sources.

## Contexts

```text
PLAYER
ADMIN
CONSOLE
RCON
AUTOMATION
GUI
NPC
SCRIPT
```

## Rule

Different contexts do not automatically require different command names.

Prefer one semantic command with context-specific input handling:

```text
/player uses current location
/console supplies --world and coordinates
```

## Context matrix

For non-trivial commands record:

| Operation | Player | Admin | Console | Automation |
|---|---|---|---|---|
| ... | allowed/restricted | ... | ... | ... |

## Player-only operations

Use only when the operation fundamentally depends on player state such as:

- current location;
- held item;
- inventory;
- visual targeting;
- player interaction.

## Console-compatible operations

Avoid silently reading player state. Require explicit equivalent inputs where possible.

## Automation

Commands triggered by GUI/NPC/Skript should not depend on interactive help or chat prompts. Prefer deterministic arguments.

## Context error

Errors should state the required context:

```text
This command requires a player because it uses your current location.
```

not a generic parser failure.
