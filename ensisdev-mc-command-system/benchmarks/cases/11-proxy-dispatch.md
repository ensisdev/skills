# Case 11 — Proxy Dispatch

## Problem

A network runs Velocity with backend `/server <name>` (local info command, legacy) colliding with the proxy `/server <name>` (cross-server travel). Players get inconsistent behavior depending on which layer answers. Separate the contracts and make scope visible.

## Scenarios

`gui-menu`, `admin-maintenance`.

## Input fixtures (OBSERVED)

```text
# observed behavior
/proxy: server lobby   -> moves player to lobby backend
/backend: /server      -> prints current server info
player typing /server lobby -> outcome depends on which layer registered first
```

## Journeys

1. player travels to lobby → exactly one layer handles it, help states which;
2. backend info still reachable under a non-colliding path;
3. proxy down → backend command degrades with documented fallback, no silent cross-talk.

## Pass criteria

Proxy vs backend modeled as separate roots per 47; no name-collision by accident; scope (local/network) in help; fallback documented; server names from registry, never hardcoded.
