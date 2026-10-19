# Case 05 — Region Admin

## Problem

A protection plugin manages named regions with flags. Admins need single-region edit plus bulk cleanup of stale shop plots (`shop-*`). Current surface: `/rg delete <name>` with no scope guard. Design explicit targets, bulk scope with preview/confirm, and audit logging.

## Scenarios

`region-protection`, `admin-maintenance`.

## Input fixtures (OBSERVED)

```java
// RegionStore (observed, simplified)
regions.delete(name);
regions.setFlag(name, flag, state);
```

```text
# console log (observed)
Admin deleted 41 regions with one command; no record of which.
```

## Journeys

1. info → set flag with explicit on/off → verify;
2. bulk delete `shop-*` with dry-run preview → confirm naming scope;
3. missing permission: moderator attempts bulk delete → denied, nothing listed.

## Pass criteria

Single vs bulk paths distinct; bulk requires explicit scope + confirm/preview + audit per 23/34; flags use explicit state; completion permission-filtered.
