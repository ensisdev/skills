# 23 — Risk and Destructive Operations

## Purpose

Classifies command risk and applies stronger controls where necessary. This is the risk taxonomy; `34-command-risk-policy.md` is the enforcement policy built on it. Read this file first.

## Risk classes

```text
READ
LOW_MUTATION
MUTATION
DESTRUCTIVE
BULK_DESTRUCTIVE
PRIVILEGED_EXECUTION
```

## READ

No persistent state change. Examples: `list`, `info`, `status`.

## LOW_MUTATION

Reversible or low-impact changes. Examples: display text, cosmetic property.

## MUTATION

Persistent changes with meaningful effect. Examples: moving a resource, changing pricing, editing permissions.

## DESTRUCTIVE

Removes or resets meaningful state. Examples: `remove`, `reset`, `clear` where recovery is not automatic.

## BULK_DESTRUCTIVE

A selector can affect many resources. The command must make scope explicit.

Preferred shape:

```text
/root remove <selector> --confirm
```

rather than an implicit wildcard.

## PRIVILEGED_EXECUTION

Operations capable of executing arbitrary player/console/server commands or temporarily escalating privileges require special review.

Never copy an `as_op` or equivalent execution model into another plugin without an explicit security assessment.

## Controls

Depending on risk, require:

- permission;
- explicit target;
- explicit state (`on|off`);
- confirmation for bulk/destructive operations;
- console-only restriction;
- audit logging;
- safe default.

## Risk output

```text
Operation: ...
Risk: ...
Controls: ...
Reason: ...
```
