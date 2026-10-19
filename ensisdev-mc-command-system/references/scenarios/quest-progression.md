# Scenario — Quest / Progression Systems

## When this scenario applies

The project manages quests, objectives, stages, rewards, completion state or player progression.

## Distinguish authoring from participation

Player commands:

```text
start
abandon
track
status
```

Author/admin commands may manage definitions:

```text
create
edit
objective
reward
publish
remove
```

Do not expose authoring operations on the player-facing command surface merely because they use the same underlying resource model.

## Ordered objectives

If order matters, use sequence-aware operations from 07 rather than treating objectives as an unordered set.

## State inspection

Separate definition metadata from player progression state. `info` on a quest definition should not silently expose another player's progress model.
