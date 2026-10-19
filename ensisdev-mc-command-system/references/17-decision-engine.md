# 17 — Command Decision Engine

## Purpose

This file owns the **decision process** for selecting a command architecture from observed project facts. It does not define all command vocabulary or framework-specific code.

## Input

The decision engine consumes:

- domain resources and relationships;
- lifecycle operations;
- property count/type;
- collection/action behavior;
- common workflows;
- current public command surface;
- compatibility constraints;
- user contexts;
- implementation framework capabilities;
- scenario matches.

## Decision sequence

### 1. Identify the target noun

Ask:

- Is the user manipulating a named resource?
- A player?
- A server setting?
- A collection?
- An event/action sequence?
- A transient action?

If a stable noun exists, use it as the target context.

### 2. Identify operation class

Classify each operation as one of:

```text
lifecycle
inspection
property mutation
collection mutation
spatial
action/trigger
system administration
migration/conversion
```

### 3. Determine namespace pressure

Use direct commands when the operation is a dominant workflow. Use a namespace such as `edit` or `action` when many sibling operations would otherwise flood the root.

### 4. Determine target repetition

If users repeatedly identify the same resource across many related operations, a resource namespace may improve predictability:

```text
/root edit <resource> ...
/root action <resource> ...
```

If a property is itself a major workflow, a direct property command may be more discoverable:

```text
/root price <shop> <amount>
```

### 5. Determine argument shape

Prefer:

```text
identity → operation details → value → modifiers
```

Move stable filters/modifiers to flags when positional arguments become ambiguous.

### 6. Determine context

Ask whether the operation differs for:

```text
player
console
automation
GUI/NPC caller
```

Do not create alternate command names merely for different actors when the semantic operation is identical.

### 7. Determine risk

Destructive/bulk/privileged operations may require confirmation, explicit selectors, permissions or context restrictions.

### 8. Compare candidates

For non-trivial redesigns create 2–3 candidates. Evaluate each against:

```text
Domain fit
Vocabulary consistency
Common-path length
Nesting clarity
Argument clarity
Completion quality
Permission clarity
Compatibility
Framework fit
Maintenance cost
```

Use labels:

```text
STRONG FIT
ACCEPTABLE
CONFLICT
REJECTED
```

Record a reason for every CONFLICT/REJECTED decision.

## Decision rules

### Direct property command
Prefer when:

- the property is a major workflow;
- there are few peer properties;
- the domain already uses that term;
- the command is frequently invoked.

### Edit namespace
Prefer when:

- the resource has many mutable properties;
- properties are conceptually grouped;
- root-level sprawl would otherwise result.

### Action namespace
Prefer when:

- an event/trigger owns an ordered list of executable actions;
- actions have add/remove/reorder semantics;
- action types are dynamic.

### Dedicated system root
Prefer when:

- the operation affects plugin/server administration rather than one resource;
- the project already has a stable administrative root.

## Tie-breaker

When two architectures are equally understandable, prefer the one that:

1. requires fewer new words;
2. better preserves compatibility;
3. exposes more useful completion context;
4. matches the project's established grammar.

Do not optimize for “cleverness.”
