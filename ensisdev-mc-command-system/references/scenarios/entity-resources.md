# Scenario — Entity / Resource Systems

## When this scenario applies

The project manages named or addressable objects with a lifecycle and mutable state: NPCs, holograms, warps, kits, arenas, portals, displays, scripted objects, etc.

## Model

```text
identity
→ create
→ inspect
→ mutate
→ duplicate
→ remove
```

## Command design

Use resource-targeting whenever several operations share the same resource identity.

Common surface:

```text
/root create <name>
/root list
/root info <resource>
/root copy <resource> <new-name>
/root remove <resource>
/root edit <resource> <property> ...
```

Do not require every lifecycle verb. Only expose observed/domain-real operations.

## Resource naming

The command argument should use the domain noun (`<npc>`, `<hologram>`, `<warp>`) and obey the project's actual naming constraints.

## Duplicate/copy

Copy must make the new identity explicit and must not silently overwrite an existing resource unless the project deliberately supports replacement.

## Inspection

`info` is for one resource. `list`/`search`/`nearby` are collection operations. Keep those meanings distinct.

## Property routing

Direct property commands are appropriate for dominant workflows. Low-frequency properties with many siblings are good candidates for `edit` grouping.

## Risks

`remove`, bulk mutations and permission-bearing resource edits require explicit capability checks. See 23 and 26.
