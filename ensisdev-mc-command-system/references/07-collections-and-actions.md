# 07 — Collections and Actions

## Purpose

Defines commands for ordered collections, trigger/action chains and similar sequence-based systems.

## Ordered list vocabulary

Use these meanings consistently:

- `add` — append an item.
- `insert_before` — insert before an index.
- `insert_after` — insert after an index.
- `set` — replace an item at an index.
- `remove` — delete one item.
- `move_up` — move one item toward the beginning.
- `move_down` — move one item toward the end.
- `clear` — delete every item.
- `list` — show the current sequence.

## Why these operations must stay distinct

`set` and `add` have different user intent. `remove` and `clear` have different blast radius. `move_up` and `move_down` communicate direction without asking users to compute a new index.

## Trigger/action architecture

Use:

```text
/root action <resource> <trigger> <operation> ...
```

when a resource can react to multiple event triggers.

Example conceptual model:

```text
NPC
  RIGHT_CLICK
    1. message
    2. command
    3. teleport
  LEFT_CLICK
    1. message
```

## Action type/value separation

An action command should distinguish:

```text
<action-type> [action-value...]
```

The action type defines behavior. The trailing value configures that behavior.

## Permission granularity

Action systems can legitimately use action-type permissions when dangerous actions differ materially from harmless ones. Do not copy this pattern into unrelated plugins without a security reason.

## Custom actions

If the project supports API-registered/custom actions, completion should discover registered types dynamically when feasible.
