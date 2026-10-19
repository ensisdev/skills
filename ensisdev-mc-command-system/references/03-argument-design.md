# 03 — Argument Design

## Purpose

Defines how values are represented and ordered. It does not define the semantic taxonomy of commands.

## Argument principles

### Put identity before mutation details

Good:

```text
/root set <resource> <property> <value>
```

Bad:

```text
/root set <value> <property> <resource>
```

unless the project has a strong reason otherwise.

### Use typed arguments

Prefer argument types that can validate at parse time:

- resource names;
- player names;
- worlds;
- locations;
- integers;
- decimals;
- booleans/states;
- enums;
- durations;
- materials/items;
- permissions;
- action types.

Do not parse a typed concept as arbitrary text and perform late manual parsing unless necessary.

### Long text

Use a greedy trailing argument for messages, MiniMessage, command payloads and similar natural-language/value strings.

### Names

Resource names should have a predictable validation rule. Preserve the project's existing naming contract when one exists.

### Indexed values

If users edit ordered collections, use one consistent index convention. Prefer a human-friendly convention such as one-based display if that matches existing project UX, while keeping internal indexing implementation-specific.

### Locations

Choose one explicit model:

- player-relative/current location;
- explicit coordinates;
- world + coordinates;
- full serialized location.

Do not mix multiple location formats invisibly.

### Optional values

An optional argument should have a useful default. Do not make arguments optional merely to avoid writing an overload.

### Boolean/state arguments

Use explicit state values when users benefit from predictability:

```text
enabled|disabled
true|false
```

Avoid commands whose meaning flips based on argument omission unless the project consistently uses that pattern.

## Argument naming

Use domain nouns, not parser implementation terms:

- `<npc>` not `<arg1>`;
- `<hologram>` not `<object>`;
- `<radius>` not `<number>`;
- `<trigger>` not `<event>` when the domain calls it a trigger.

The argument label is part of documentation and completion UX.
