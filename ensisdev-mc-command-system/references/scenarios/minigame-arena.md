# Scenario — Minigame and Arena Systems

## When this scenario applies

The project runs matches: arenas, lobbies, queues, teams, kits, match states (waiting → starting → running → ending).

## Domain distinctions

Keep these separate:

```text
arena identity and lifecycle (create, enable, disable, delete)
match control (start, stop, force-end)
player flow (join, leave, spectate, queue)
match configuration (teams, kits, spawnpoints, settings)
inspection (status, list, leaderboard)
```

## Common command design

Player flow favors short verbs on the game root:

```text
/arena join <arena>
/arena leave
/arena list
```

Match control and configuration are admin-gated, often with explicit state:

```text
/arenaadmin start <arena>
/arenaadmin stop <arena> --confirm
/arenaadmin set <arena> lobby
```

## State rule

Match-state transitions are explicit and guarded: `start` on a running match is a domain error stating current state, not a silent restart. `force-end`/`stop` during a live match is `destructive` (23/34) with confirmation naming the match.

## Collections

Spawnpoints, teams and kits are ordered/named collections — sequence semantics from 07 apply (`add`, `set`, `remove`, `clear`, `list`). Player-count limits and team balance rules are validated arguments with domain errors, not parse crashes.
