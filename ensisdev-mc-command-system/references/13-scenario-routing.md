# 13 — Scenario Routing

## Purpose

Routes observed project structures to domain playbooks and the architectural references that should be loaded with them.

## Detection matrix

| Signal | Scenario | Load with it |
|---|---|---|
| named persistent objects/entities | `entity-resources.md` | 05, 06, 08, 09, 11, 12 |
| coordinates, rotation, radius, nearby | `spatial-systems.md` | 03, 04, 10, 11, 23, 24 |
| event → ordered actions | `action-trigger-systems.md` | 07, 11, 23, 26 |
| player-facing gameplay loops | `gameplay-player.md` | 03, 08, 10, 11, 24 |
| reload/save/debug/convert | `admin-maintenance.md` | 08, 09, 10, 23, 25 |
| inventories, menus, views | `gui-menu.md` | 03, 10, 21, 22, 24 |
| products, currencies, prices | `economy-shop.md` | 05, 06, 09, 23, 26 |
| claims/regions/bounds | `region-protection.md` | 03, 04, 09, 10, 23, 24 |
| tasks/quests/progression | `quest-progression.md` | 05, 06, 07, 08, 11, 21 |
| Skript commands/functions | `scripting.md` | 14, 22, 24, 25 |
| travel/teleport/warps/homes | `teleport-travel.md` | 03, 10, 23, 24, 45, 49 |
| moderation/punishment | `moderation-punishment.md` | 03, 09, 23, 26, 34 |
| minigame/arena/match | `minigame-arena.md` | 05, 06, 07, 09, 23 |

## Secondary signals

Also route:

```text
collections → 07
rich mutable resources → 06 + 18
many aliases → 12 + 19
many integrations → 29 + 30 + 50
multiple frameworks → 27
multiple MC versions → 46
Folia/async work → 45
proxy commands → 47
charged/cooldown commands → 49
manifest-declared commands → 52
public command rename → 12 + 20 + 25 + 21 + 43 + 44
arbitrary command execution → 23 + 26 + 24
```

## Multi-scenario rule

Compose playbooks instead of choosing one winner. The final architecture is the intersection of the project's actual domain model and the relevant scenario guidance.

## Scenario precedence

When scenario guidance conflicts, use:

1. observed project behavior;
2. existing documented public API;
3. security/compatibility constraints;
4. primary user workflow;
5. domain semantics;
6. generic skill preference.
