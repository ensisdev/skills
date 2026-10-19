# 25 — Documentation and Command Surface Synchronization

## Purpose

Keeps command implementation, help, completion and public documentation consistent.

## Single semantic source

When possible, derive these from the same command AST/model:

```text
syntax
help
completion
permissions
documentation
migration notes
```

## Search before editing

Search for old command strings in:

- README files;
- docs/wiki;
- tests;
- examples;
- config;
- Skript files;
- GUI/NPC/hologram action definitions;
- source code;
- generated resources.

## Drift classes

### Missing documentation
Implementation has a public command not documented.

### Stale documentation
Docs show a command that no longer exists or changed syntax.

### Alias drift
Docs use an alias rather than the canonical command without saying so.

### Permission drift
Documentation states a command exists but omits the required permission or lists an obsolete node.

### Completion drift
Completion offers commands/values that no longer exist.

## Synchronization order

1. Final semantic model.
2. Command AST.
3. Implementation.
4. Help/completion.
5. Docs/examples.
6. Migration notes.

## Output

```text
DOCUMENTATION SYNC
Status: CLEAN | DRIFT FOUND | BLOCKED
Files checked: ...
Stale references: ...
Missing references: ...
```
