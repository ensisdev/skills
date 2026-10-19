# Scenario — Spatial Systems

## When this scenario applies

The project manipulates locations, coordinates, rotation, radius, nearby objects, worlds or spatial relationships.

## Mandatory semantic distinction

Never let `move` and `teleport` silently swap actors.

Example:

```text
move_here(resource) = move the resource to the executor
teleport(resource) = move the executor to the resource
move_to(resource, location) = move the resource to a specified location
```

Use project vocabulary if it already has an established naming scheme, but preserve direction clarity.

## Location inputs

Choose a small set of explicit location models:

```text
current player location
explicit x y z
world + x y z
full location object
```

Do not make console use depend on a hidden player location.

## Nearby/listing

`nearby` should make its spatial scope explicit, usually via radius or a project default. Filters belong naturally in flags.

## Rotation

Separate rotation from movement when they are independent operations.

## Completion

Worlds, online players, known locations and resource names should come from authoritative runtime sources where possible.
