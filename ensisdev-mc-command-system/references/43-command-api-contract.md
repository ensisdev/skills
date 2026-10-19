# 43 — Command API Contract

## Purpose

Treats public commands like a versioned API: every user-visible behavior is a contract dimension, and every contract change needs an explicit compatibility disposition.

## Contract dimensions

```text
path                 the literal token sequence, e.g. hologram edit <name> lines add
argument meaning     what each positional/greedy argument denotes
argument order       positional order is contract; reordering is breaking
aliases              every alias is contract, including undocumented-but-used ones
permission semantics which capability each node grants (renames are breaking for managers)
context support      player/console/command-block/rcon support per node
output expectations  machine-readable output shapes used by integrations (JSON, hook events)
error semantics      which failures are usage errors vs domain failures, and their messages
completion behavior  which values complete, filtered by permission
```

## Change classification

```text
additive      new leaf/flag that does not alter existing paths        -> minor, document
clarification help/completion improvement with identical parsing       -> patch, document
alias         old path resolves to identical semantics                -> minor, record mapping
deprecation   old path warns and forwards, removal scheduled          -> minor, schedule removal
breaking      path/arg-order/permission/context change                -> major, migration plan required
```

## Compatibility disposition

Every changed path gets exactly one disposition, recorded in the AST `deprecation` metadata:

```yaml
deprecation:
  old_path: shop create <name>
  disposition: alias        # preserve | alias | deprecate | migrate | remove
  forwards_to: shop add <name>
  removal_version: 3.0     # required for deprecate
  reason: canonical verb unification (19)
```

`remove` is allowed only when evidence shows the path is undocumented, unreferenced by integrations/scripts/tests, and the project policy permits removal. Otherwise use `alias` or `deprecate`.

## Contract record

```yaml
contract:
  version: 2.4.0
  roots: [shop, shopadmin]
  breaking_changes_since_last: []
  deprecated_paths: []
  removal_schedule:
    - path: shop create <name>
      remove_in: 3.0
```

Review the contract record in every Phase 14 audit.
