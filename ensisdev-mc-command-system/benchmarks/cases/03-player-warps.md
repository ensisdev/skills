# Case 03 — Player Warps

## Problem

A warp plugin has one flat root: `/warp <name>`, `/warp set <name>`, `/warp del <name>`, `/warplist`. Warp travel costs $50 with a 10s cooldown. Separate player travel flow from admin catalog management, make cost/cooldown visible, keep `/warp <name>` working.

## Scenarios

`teleport-travel`, `gameplay-player`.

## Input fixtures (OBSERVED)

```yaml
# plugin.yml (observed)
commands:
  warp:
    description: Warp commands.
```

```text
# config.yml (observed)
travel-cost: 50
travel-cooldown-seconds: 10
```

## Journeys

1. list → go (charged, confirm) → arrive;
2. insufficient funds → domain error stating cost and balance;
3. cooldown active → error stating remaining wait;
4. compatibility: `/warp <name>` shortcut preserved.

## Pass criteria

Direction explicit (go-to); cost/cooldown in help + confirm prompt + errors per 49; admin verbs namespaced or permission-tiered; teleport declares thread affinity per 45.
