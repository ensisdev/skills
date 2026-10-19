# Scenario — Action / Trigger Systems

## When this scenario applies

A resource owns one or more triggers/events, and each trigger contains an ordered list of executable actions.

## Model

```text
resource
  → trigger
      → ordered action sequence
```

## Canonical sequence operations

```text
list
add
insert_before
insert_after
remove
move_up
move_down
clear
```

Not every project needs every operation.

## Action type

Action types should complete from the project's actual registry. Do not hard-code examples if the implementation supports dynamic action registration.

## Value parsing

Action values are often greedy trailing input. Preserve the action type as a typed token and avoid parsing every payload as a single undifferentiated string.

## Security

Actions that execute player/console commands or elevated operations are privileged execution. Apply 23 and 26.

## Reordering

If order changes behavior, show indices consistently and make reorder operations explicit.

## Completion

Completion should be context-aware at every layer:

```text
resource → trigger → sequence operation → action type → action value
```
