# Case 10 — Confirm Destructive Admin

## Problem

An admin plugin offers `/purge inactive <days>` deleting all player data older than N days, currently executing immediately with no scope statement. Redesign with preview, named-scope confirmation, expiry and audit — while keeping a scriptable non-interactive path for scheduled automation.

## Scenarios

`admin-maintenance`.

## Input fixtures (OBSERVED)

```java
// PurgeTask (observed, simplified)
store.deleteWhere(lastSeenOlderThan(days));
sender.sendMessage("Purged.");
```

## Journeys

1. dry-run → states matched count before anything is deleted;
2. confirm within window → executes, audit log records actor/scope/result;
3. expired confirm → must re-issue, never executes stale intent;
4. scheduler automation → non-interactive `--confirm` flag path.

## Pass criteria

`bulk-destructive` with explicit scope + preview + expiring two-step confirm per 23/34; prompt names scope; audit metadata in AST; interactive and automation paths distinct.
