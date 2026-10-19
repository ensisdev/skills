# Scenario — Teleport and Travel Systems

## When this scenario applies

The project moves players through space: warps, homes, spawns, teleports, portals, elevators.

## Domain distinctions

Keep these separate:

```text
destination identity (named warp/home vs coordinates vs player target)
travel initiation (request, instant, delayed with warmup)
cost (free, economy charge, item cost, cooldown, xp levels)
safety (safe-teleport resolution, claim checks, combat-tag blocking)
direction (go-to vs bring-here vs send-to — never ambiguous)
```

## Common command design

Player workflows favor short direct verbs:

```text
/warp <name>
/warp list
/home [name]
/spawn
/tpa <player> | /tpaccept | /tpdeny
```

Administration favors a resource namespace:

```text
/warpadmin create <name>
/warpadmin move <name>
/warpadmin delete <name>
```

## Direction rule

Every teleport leaf names its direction explicitly in syntax and help:

```text
/tp <player>            bring HERE (documented)
/tp <a> <b>             send a TO b (admin-only)
/warp go <name>         go TO warp
```

A teleport command whose help does not state who moves where is incomplete.

## Safety and cost

- Warmup/cancel-on-move and combat-tag rules are contract (43): state them in help and errors.
- Charges and cooldowns follow 49: cost in help, exact wait in errors.
- Cross-region/world teleports on Folia follow 45 thread affinity.
- Admin teleport of others is `mutate` risk minimum with explicit target (23).
