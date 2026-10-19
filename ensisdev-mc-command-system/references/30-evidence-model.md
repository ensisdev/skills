# 30 — Evidence Model

## Purpose

Prevents unsupported assumptions during command redesign.

## Evidence classes

### OBSERVED
Directly supported by the project or verified reference material.

Examples:

```text
plugin.yml registers /npc
```

```text
NpcManager.delete(npc) exists
```

### INFERRED
A reasoning step derived from observed evidence.

Example:

```text
NPC is likely a durable resource because it has persisted identity and remove/list operations.
```

### PROPOSED
A new architecture recommendation.

Example:

```text
Use /npc edit <npc> for low-frequency property mutations.
```

## Confidence

For non-trivial decisions record:

```text
high
medium
low
```

Confidence is about evidence strength, not whether a design is aesthetically preferred.

## Rule

Never write:

```text
The plugin uses /npc edit
```

when the repository only supports:

```text
Observed: NPC properties are mutable.
Proposed: /npc edit could group low-frequency property mutations.
```

## Evidence ledger

Use a compact ledger:

```text
ID | Claim | Class | Evidence | Confidence
```

This ledger is especially useful when a redesign changes public syntax.
