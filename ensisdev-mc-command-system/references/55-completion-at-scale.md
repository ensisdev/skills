# 55 — Completion at Scale

## Purpose

Engineering companion to `11-tab-completion.md`. Principles say what to complete; this file says how to survive 10k+ candidates without lagging the server or leaking data.

## Source strategy per argument kind

```text
static enum (< dozen)      hardcode in the parser; zero cost
registry snapshot          copy names on change events, serve from memory (warps, homes, regions)
online players             server list call is already cheap; filter by prefix early
worlds/locations           never enumerate blocks; complete named anchors only
history/fuzzy              rank by recent use, then prefix match; cap at 25 shown
```

## Performance rules

1. **Never query the database in a suggestion provider.** Serve from the snapshot; a stale-by-seconds list beats a lag spike.
2. **Prefix-filter before permission-filter** on large sets, then permission-filter the top N — but never show an unauthorized entry (11 is absolute).
3. **Cap displayed suggestions** (default 25) with a deterministic order; document the ordering (alphabetical vs recent-first) in help.
4. **Async-safe providers only**: no region-locked state, no lazy loading on the netty/completion thread (45).
5. **Cache invalidation is explicit**: registry mutations (create/remove) invalidate the snapshot in the same transaction that persists them.

## Large-set UX

- Beyond the cap, the list footer states scope: `showing 25 of 1,204 — keep typing to narrow`.
- Fuzzy matching is opt-in per leaf and documented; default is prefix match so behavior is predictable.
- Numeric/range arguments complete nothing but validate with bounds errors (typed > completable).

## Test hook

Per 51: completion tests use a seeded registry of 10k+ entries and assert response time budget plus exact permission-filtered output. A provider that is correct on 10 entries and slow on 10k fails review.
