# SOUND UX — Auditory Feedback Layer

Half of Minecraft's interface feel is auditory. A visually perfect menu that plays
no sound feels broken; one that plays the right sound at the right moment feels
finished. Treat sound as a designed surface, not an afterthought.

---

## 1. Semantic sound roles

Assign sounds to roles once, plugin-wide — same discipline as color roles:

| Role | Meaning | Vanilla candidates (pitch/vol tuned) |
|---|---|---|
| confirm | transaction succeeded | `ENTITY_EXPERIENCE_ORB_PICKUP` (high pitch) |
| open | menu/screen opened | `BLOCK_CHEST_OPEN`, `BLOCK_BARREL_OPEN` |
| close | screen dismissed | `BLOCK_CHEST_CLOSE` (quieter) |
| deny / error | action refused | `ENTITY_VILLAGER_NO` (low pitch) |
| warning | attention needed | `BLOCK_NOTE_BLOCK_BASS` ×2 |
| select | highlight changed | `UI_BUTTON_CLICK` (subtle) |
| claim/reward | something received | `ENTITY_PLAYER_LEVELUP` (soft, vol 0.4) |
| page turn | pagination moved | `ITEM_BOOK_PAGE_TURN` |
| countdown tick | final seconds urgency | `BLOCK_NOTE_BLOCK_HAT` ascending pitch |
| ready | cooldown finished | `BLOCK_NOTE_BLOCK_PLING` |

Pick ONE sound per role. Never assign two meanings to one sound.

## 2. Pitch and volume as micro-semantics

- **Pitch encodes magnitude:** higher stack size / bigger purchase → slightly higher
  pitch (`0.9f + min(amount/10000f, 0.4f)`).
- **Volume encodes distance to importance:** global broadcast = 1.0f; personal
  feedback = 0.5–0.7f so nearby players are not spammed.
- Ascending pitch sequences communicate progress toward a goal; descending ones
  communicate decay/expiry.

## 3. Rules

001. Silence is a valid choice — ambient screens need no loop.
002. Never attach sound to hover-like frequent events (inventory dragging).
003. Rate-limit identical cues per player (e.g., max 1/s) even if the event repeats.
004. Error sounds must accompany a visible message, never replace one.
005. Reward sounds must not fire for zero-value outcomes.
006. Respect the server's atmosphere: a hardcore survival plugin should not use
     playful note-block melodies everywhere.
007. Sounds are additive feedback, never the sole carrier of state (accessibility).
008. Document the role→sound mapping in `design-system.yml` (see code patterns §13).

## 4. Anti-patterns

- `LEVEL UP` fanfare on every button click (reward inflation → meaning erosion)
- Same sound for success and error (semantic collision)
- Global sound for personal transactions (spatial noise)
- Countdown ticks that continue after the timer ends

## 5. Design review questions

- Which of my surfaces have no auditory identity at all?
- Does every sound I play answer "what just happened?"
- Would a blindfolded player understand the outcome from audio alone?
- Am I within the rate limits during burst actions (bulk claiming)?
