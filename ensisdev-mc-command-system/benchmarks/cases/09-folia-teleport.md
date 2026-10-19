# Case 09 — Folia Teleport Safety

## Problem

A teleport plugin runs on Folia. `/tpo <player>` teleports the executor to the target across regions; `/tpohere <player>` brings the target to the executor. A naive port calls teleport off-thread and corrupts cross-region moves. Design the tree with explicit direction and thread-affinity metadata.

## Scenarios

`teleport-travel`, `spatial-systems`.

## Input fixtures (OBSERVED)

```java
// TeleportService (observed, simplified)
player.teleport(target.getLocation()); // called from command handler directly
```

```text
# build.gradle (observed)
paper-version: 1.21, folia-supported: true
```

## Journeys

1. teleport to player in another region → arrives, no errors;
2. bring-here with missing permission → denied before any scheduler hop;
3. console sends player A to player B → works without executor location.

## Pass criteria

Direction explicit per leaf; every region-touching leaf declares `thread_affinity: region` + scheduler per 45; permission checked before async work; console variant takes explicit targets.
