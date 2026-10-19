# PERFORMANCE NOTES — Design Decisions and Their Technical Cost

Every visual refresh costs packets and CPU. These constraints shape what designs
are actually shippable. Read alongside COMPATIBILITY.md.

---

## 1. Inventory GUIs

| Practice | Cost | Guidance |
|---|---|---|
| Full re-open on data change | re-sends all items + flicker | ❌ never for live updates |
| Clear-all → refill loop | visible flicker, GC churn | ❌ anti-pattern |
| Targeted `setItem` on changed slots | 1 slot diff | ✅ default |
| Title change per update | window close/reopen animation | ⚠️ avoid mid-session; use in-GUI status row instead |

- Live price/stock updates: batch at 500–1000 ms; players cannot read faster.
- Pagination: build pages lazily and cache immutable item arrays.
- Cursor interactions (drag-splitting) need no plugin feedback sounds — see SOUND_UX rule 002.

## 2. Scoreboard

- Line limit: 16 visible lines (plus title); pre-1.13 text length limits forced
  team-prefix tricks — know your floor version (COMPATIBILITY §1).
- Naive per-line rewrite every tick = packet flood. Batch to 500–1000 ms and only
  when values changed (dirty-flag).
- Flicker-free pattern: keep one Objective, update scores/team prefixes in place;
  never unregister/recreate the Objective per update.
- Design implication: scoreboard content must be a small, stable set of values —
  this is why rules/TACTICAL_GUIDE.md §15 demands grouping and stability.

## 3. Action bar / Boss bar

- Action bar: max ~2 updates/sec; it overwrites itself, so competing systems
  (protection timer vs combat tag) will fight — route through ONE presenter with
  priority.
- Boss bar: progress float updates are cheap but still rate-limit (≥200 ms);
  color/title changes are fine at phase boundaries, not per-tick.

## 4. Tab list

- Header/footer: static by default; dynamic player counts at ≤1 Hz.
- Per-player list name changes cost a player-info packet each — do not animate.

## 5. Chat

- Broadcasts: queue + throttle; a burst of 10 lines pushes real chat off-screen,
  which is also a UX failure (rules/TACTICAL_GUIDE.md §12 compactness rules exist partly for this).
- Hover-rich components are fine; component tree depth affects serialization cost
  only at extreme scale — prioritize clarity over micro-optimizing depth.

## 6. Holograms

- Prefer TextDisplay entities (1.19.4+): cheaper, no armor stand head/body packets.
- Update text at most 1–2 Hz; holograms are glanceable (EX-22), not dashboards.
- Spawn once, reuse; despawn cleanly on chunk unload if not persistent.

## 7. Caching & immutability

```kotlin
// Build reusable Components once; Components are immutable
private val HEADER by lazy { Component.text("ᴘᴀᴢᴀʀ", Theme.brand) }
```
- Cache rendered templates per locale, invalidate only when config reloads.
- Do not rebuild identical lore lists per inventory click.

## 8. Budget summary (defaults)

| Surface | Max refresh rate | Trigger |
|---|---|---|
| Inventory slots | 1–2 Hz | data change only |
| Scoreboard | 0.5–1 Hz | dirty flag |
| Action bar | 2 Hz | presenter priority |
| Boss bar progress | ≤5 Hz | smooth progress needs |
| Tab header/footer | ≤1 Hz | count change |
| Hologram text | 1–2 Hz | state change |

A design that requires exceeding these budgets is a design flaw — simplify the
surface instead of spamming packets.
