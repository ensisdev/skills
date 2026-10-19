# 28 — Command AST Specification

## Purpose

Defines the semantic representation of a command tree. This file is the contract between architecture design and implementation.

## Minimal node model

```yaml
root: npc
nodes:
  - path: npc create
    kind: lifecycle
    operation: create
    actor: [ADMIN, CONSOLE]
    permission: plugin.npc.create
    risk: MUTATION

  - path: npc info <npc>
    kind: inspection
    operation: info
    arguments:
      - name: npc
        type: resource:npc
        required: true
```

## Node fields

```text
path
kind
operation
parent
children
arguments
flags
aliases
contexts
permissions
risk
completion
help
errors
compatibility
notes
```

## Argument node

```yaml
arguments:
  - name: radius
    type: decimal
    required: false
    default: 16
    constraints:
      min: 0
```

## Flag node

```yaml
flags:
  - name: radius
    type: decimal
    required: false
```

## Completion metadata

Completion should state where values come from:

```text
static enum
runtime resource registry
online player registry
world registry
permission filtered
context filtered
```

## Permission metadata

Permissions attach to capabilities, not implementation classes.

## Risk metadata

Each mutating node has a risk class from `23-risk-destructive-operations.md`.

## Compatibility metadata

Legacy command paths can point to a canonical node:

```yaml
compatibility:
  aliases:
    - oldroot oldverb <name>
  canonical: root newverb <name>
```

## AST invariants

1. Every public command path resolves to exactly one semantic operation.
2. An alias must resolve to a canonical node.
3. Every typed argument has validation information.
4. Every mutation has a risk class.
5. Every restricted operation has a permission model.
6. Completion never invents values not accepted by the parser.
7. Help syntax must be derivable from the node structure.
8. Compatibility aliases cannot implement a second code path unless technically unavoidable.

## AST example: NPC actions

```yaml
root: npc
action:
  path: npc action <npc> <trigger> <operation>
  children:
    add:
      arguments:
        - name: action_type
          type: enum:registered_action_type
        - name: value
          type: greedy_text
          required: false
    remove:
      arguments:
        - name: index
          type: integer
    move_up:
      arguments:
        - name: index
          type: integer
    move_down:
      arguments:
        - name: index
          type: integer
    clear: {}
    list: {}
```

## Storage rule

If the host project can centralize command metadata, prefer one AST-backed definition over manually duplicating syntax in registration, help and docs.
