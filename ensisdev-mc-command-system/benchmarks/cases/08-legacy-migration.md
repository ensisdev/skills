# Case 08 — Legacy Migration

## Problem

A v1 plugin has flat inconsistent roots: `/sethome`, `/delhome`, `/homes`, `/home <name>`, plus `/adminhome <player> <name>` for staff. Migrate to one coherent tree for v2 with deprecation warnings, a removal schedule, and updated docs — without breaking v1 player muscle memory on day one.

## Scenarios

`teleport-travel`, `admin-maintenance`.

## Input fixtures (OBSERVED)

```yaml
# plugin.yml v1 (observed)
commands:
  sethome: {}
  delhome: {}
  homes: {}
  home: {}
  adminhome: {}
```

```text
# docs/v1.md (observed)
Set a home with /sethome, go with /home <name>, delete with /delhome.
```

## Journeys

1. v1 player types `/sethome` → works, deprecation notice names `/home set`;
2. staff inspects another player's home → permission-gated admin path;
3. docs updated; old paths scheduled for removal with version.

## Pass criteria

One canonical tree; every v1 path dispositioned (alias/deprecate) per 43/44 with removal version; deprecation messages name the replacement; staff vs player paths separated by capability.
