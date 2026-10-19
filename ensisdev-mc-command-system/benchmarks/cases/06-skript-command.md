# Case 06 — Skript Command

## Problem

A Skript file defines `/kit <name>` giving items, plus an undocumented `/kit reload` that re-parses the script. Console dispatch from a scheduler calls `/kit give <player> <kit>` which does not exist as a path. Rationalize player vs admin vs automation surfaces in Skript-idiomatic form.

## Scenarios

`scripting`, `gameplay-player`.

## Input fixtures (OBSERVED)

```applescript
# kits.sk (observed)
command /kit <text>:
  trigger:
    give player kit arg-1
```

```text
# scheduler config (observed)
run: "kit give {player} starter" every 24h
```

## Journeys

1. player claims kit → cooldown error with remaining time on repeat;
2. invalid kit name → domain error listing available kits;
3. automation dispatch works without a fake player session.

## Pass criteria

Player/admin/automation paths distinct with declared executors per 14; parser vs domain failures produce different messages; cooldown follows 49; scheduler caller migrated per 50.
