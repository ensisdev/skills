# 20 — Command Collision and Namespace Resolution

## Purpose

Prevents conflicts with other plugin commands, aliases and generic words.

## Collision classes

1. Root command collision.
2. Alias collision.
3. Permission namespace collision.
4. Semantic collision with an existing command.
5. Integration collision where another system invokes a command by string.
6. Documentation collision where two features use the same public term.

## Investigation

Inspect:

- plugin.yml/paper-plugin.yml or equivalent;
- command registrations;
- aliases;
- tests and fixtures;
- documentation;
- commands dispatched by the plugin;
- known companion plugins/integrations visible in the repository.

Do not assume a generic name is safe because the current code compiles.

## Resolution strategy

### Prefer domain qualification

Prefer:

```text
/npc info
/shop list
/warp create
```

over unqualified:

```text
/info
/list
/create
```

### Preserve project root

If a project already has a stable root, do not invent another root just to solve a low-level collision.

### Aliases

An alias is acceptable when:

- it points to the same semantic operation;
- it does not create ambiguity;
- it is cheaper than a breaking rename.

### Unresolvable collision

If the desired root is already occupied and a project-specific namespace is necessary, document the reason. Do not silently take over a common root.

## Collision output

```text
COLLISION REVIEW
Root: /...
Status: CLEAR | COMPATIBLE | CONFLICT
Evidence: OBSERVED | INFERRED
Resolution: ...
```
