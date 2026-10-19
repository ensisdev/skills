# 06 — Property Editing

## Purpose

Defines how resource properties are exposed as commands. It does not own resource creation or ordered collections.

## Three property strategies

### Strategy A — Direct property commands

Use when a property is a dominant workflow:

```text
/resource name <resource> <text>
/resource skin <resource> <skin>
/resource price <item> <amount>
```

This is appropriate when users regularly remember and type the property command.

### Strategy B — Edit namespace

Use when a resource has many peer properties:

```text
/resource edit <resource> <property> <value>
```

This keeps the root clean and makes the resource target explicit.

### Strategy C — Nested domain namespaces

Use when the property is actually a distinct sub-domain:

```text
/resource action <resource> <trigger> ...
/resource attribute <resource> <attribute> ...
```

Do not force every feature under `edit` merely for symmetry.

## `set` vs `edit`

Use `set` when the command represents a single explicit assignment operation.

Use `edit` as a namespace when it contains multiple property operations.

Do not create:

```text
/edit set
```

unless `edit` is itself a real domain concept.

## Resetting properties

Use one clear reset semantic:

- `clear` when removing collection content;
- `reset` when restoring a defined default;
- a sentinel such as `none` only when the domain meaning is truly "no value" and the project already uses this convention.

## Property grouping

Group properties by user mental model, not Java field layout.

For example:

```text
location
appearance
interaction
visibility
attributes
```

may be more useful than:

```text
data1
data2
metadata
flags
```

## Type-specific properties

If a resource has variants, prefer command availability and completion that follow the actual variant capabilities. Do not expose commands that cannot apply to the selected resource type.
