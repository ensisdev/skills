# 45 — Folia and Threading Safety

## Purpose

Keeps command architecture correct on Folia (region-threaded) and on any Paper/Spigot project doing async work. Threading constrains implementation and context support; it must be visible in the AST, not discovered in production.

## What changes on Folia

```text
Bukkit scheduler global         -> Folia GlobalRegionScheduler / AsyncScheduler
entity/teleport/world access    -> must run on the entity's region thread (EntityScheduler)
shared mutable state in handler -> region contention or races; prefer per-region or async-safe stores
sync-only API calls             -> illegal off-thread; teleport, inventory, most world mutation
```

## Command design consequences

- **Declare thread affinity per leaf** in AST `implementation` metadata: `region`, `global`, or `async-safe`.
- Region-touching commands (`teleport`, `move`, `spawn`, inventory mutation) must execute on the owning scheduler. The command tree does not change, but the adapter must route execution — record the routing decision.
- Bulk selectors (`all`, `nearby <radius>`) can span regions. Prefer chunked/queued execution with progress output over one blocking pass.
- Confirmation state (`44`) must be thread-safe storage, never a plain HashMap assumed single-threaded.
- Completion providers must not touch region-locked state; serve from snapshots/registries.

## Forensics signals

```text
Folia
RegionScheduler
GlobalRegionScheduler
AsyncScheduler
getScheduler()
runAtFixedRate
runDelayed
isOwnedByCurrentRegion
```

If any appear, load this file and review every mutating leaf for affinity.

## Async discipline (all platforms)

- Parse/validate on the calling thread; switch threads only for the domain effect.
- Never hold a `CommandSender` across an async boundary without checking validity on return.
- Database/I-O bound leaves (`lookup`, `history`, `convert`) state their async behavior in help when latency is user-visible.
- Errors from async work must still resolve to the 08 error taxonomy (usage vs domain failure), not raw stack traces.

## AST record

```yaml
implementation:
  thread_affinity: region      # region | global | async-safe
  scheduler: entity            # entity | global-region | async | bukkit-sync
  notes: teleport runs on target entity scheduler
```
