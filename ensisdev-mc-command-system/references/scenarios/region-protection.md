# Scenario — Region / Protection Systems

## When this scenario applies

The project manages named protected regions, claims, boundaries, flags or access rules.

## Domain model

Typical entities:

```text
region
owner/member
boundary
flag/policy
permission
priority/overlap
```

## Selection

Region identity should be explicit before changing a region's flags or members.

## Spatial grammar

Creation can be player-location driven or explicit coordinate based. Console-compatible creation needs a deterministic location form.

## Flags

Use flags for optional policy modifiers only if the domain naturally treats them as a named set of values. Do not confuse command flags such as `--world` with region policy flags.

## Destructive operations

Region removal and bulk member/flag changes are high impact. Require appropriate capabilities and explicit targets.
