# 22 — Semantic Mapping: Code → User Operations

## Purpose

Translates implementation concepts into user-facing operations without leaking internal architecture.

## Mapping pipeline

```text
code symbol
  ↓
behavioral meaning
  ↓
domain concept
  ↓
user intent
  ↓
command operation
```

## Example

Observed:

```text
HologramManager.clearLines(hologram)
```

Behavior:

```text
empties the hologram's line collection
```

Domain concept:

```text
hologram content
```

Possible public forms:

```text
/hologram clear-lines <hologram>
/hologram edit <hologram> lines clear
```

The choice depends on command architecture, workflow frequency and existing vocabulary.

## Internal-to-public anti-patterns

Do not expose:

- manager names;
- service names;
- repository/database terms;
- DTO/model names;
- setter method names;
- implementation lifecycle hooks.

unless the project intentionally defines those as domain concepts.

## Rename check

If internal methods and public terminology disagree, preserve the public terminology unless the user-facing term itself is defective and compatibility cost is acceptable.

## Mapping table

For non-trivial redesigns maintain:

```text
Observed code | Behavioral meaning | User intent | Canonical command | Evidence
```
