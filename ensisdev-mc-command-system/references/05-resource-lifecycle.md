# 05 — Resource Lifecycle

## Purpose

Defines command design for durable named resources. This file owns lifecycle semantics only.

## Lifecycle model

A resource-oriented plugin commonly has:

```text
create → exist → inspect/edit → copy → remove
```

Not every project needs every operation.

## `create`

Use for creating a new persistent or server-recognized resource.

Requirements:

- establish a unique identity where applicable;
- validate required creation inputs;
- choose sensible defaults;
- show enough feedback to confirm the resulting identity/location.

Avoid forcing users to immediately execute a second command for values that are essential to creation if a clean creation syntax can accept them.

## `copy`

Use when copying a resource retains meaningful structure and relationships.

It should normally require:

```text
<source> <new-name>
```

Do not use `copy` for an operation that intentionally converts the resource into a different domain type.

## `remove`

Use for permanent deletion/removal.

For destructive bulk operations, require an explicit confirmation mechanism.

## `list`

Use to enumerate the resource collection. Provide filters and sorting only when useful to real administration workflows.

## `info`

Use for one-resource inspection. `info` should emphasize facts that help administration/debugging:

- identity;
- location;
- type;
- key properties;
- relationships;
- runtime status when relevant.

## `nearby`

Use only for spatial resources. It answers "what resources are around the executor?" and should not be used as a generic filter name.

## `find` / `search`

Use when discovery is fundamentally textual or semantic rather than a simple list.

## Resource identity

A resource should be addressable consistently by one canonical identifier type. Do not make users alternate unpredictably between name, numeric ID, UUID and display name.

## Lifecycle command ordering in help

Place `list`, `info`, `create`, `copy`, mutation, then `remove` according to the project's actual workflow. The exact order is UX, not a hard syntax rule.
