# Case 02 — NPC Actions

## Problem

An NPC plugin attaches ordered action lists to interaction triggers (click, proximity). Current surface: `/npc action add <npc> <cmd>`, `/npc action del <npc> <n>`, `/npc action list <npc>`. Add reorder semantics and per-action-type permissions without breaking existing scripts that dispatch these commands from GUIs.

## Scenarios

`entity-resources`, `action-trigger-systems`.

## Input fixtures (OBSERVED)

```java
// NpcActions (observed, simplified)
actions.add(npc, trigger, actionString);
actions.remove(npc, trigger, index);
```

```text
# gui/menus.yml (observed)
click-actions:
  - "npc action add guard greet"
```

## Journeys

1. add `message` action → list → move up → remove;
2. permission-denied: moderator without action-type permission adding `console-command` action;
3. compatibility: GUI-dispatched old `del` path still works.

## Pass criteria

Ordered sequence semantics (add/insert/remove/move/list/clear per 07); trigger vs action distinct; privileged action types (`console-command`) gated per 23/26; GUI caller migrated or aliased per 50/44.
