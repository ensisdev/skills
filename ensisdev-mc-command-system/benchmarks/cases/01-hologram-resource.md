# Case 01 — Hologram Resource

## Problem

A plugin manages persistent named holograms with text lines, location, rotation, scale and background. The current surface grew organically: `/hd create`, `/hd setline`, `/hd moveto`, `/hd delete`, `/hd list`. Redesign into a coherent resource tree preserving the documented paths as aliases.

## Scenarios

`entity-resources`, `spatial-systems`.

## Input fixtures (OBSERVED)

```yaml
# plugin.yml (observed)
commands:
  hd:
    description: Hologram commands.
    aliases: [hologram]
```

```java
// HologramManager (observed, simplified)
hologramManager.create(name, location);
hologramManager.setLine(hologram, index, text);
hologramManager.moveTo(hologram, location);
hologramManager.delete(name);
```

```text
# README (observed)
Use /hd create <name> then /hd setline <name> <index> <text>.
```

## Journeys

1. create hologram → add line → set background → move to executor position;
2. invalid input: set line index out of range → usage/domain error;
3. compatibility: old `/hd setline` still resolves.

## Pass criteria

Lifecycle separated from property mutation; spatial direction explicit (`moveHere` vs `moveTo` or equivalent); old paths dispositioned per 43/44; every mutation risk-classed.
