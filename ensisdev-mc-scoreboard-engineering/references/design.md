# Design reasoning and score anchors

## Information first

A sidebar is peripheral while playing: optimize for a one-second glance. Include a value only if it changes a decision, confirms progress, or reinforces server identity. Survival might show money, region, online count and a command hint; a match server might show round, team, objective and time. TAB can carry broader context, but its header/footer should remain short while the player list stays readable. Prefer stable placement as numbers update.

Ask “what would a player miss if this row disappeared?” Remove rows without an answer. Brand can appear once prominently; repeated addresses rarely help. Reserve an accent for state or headings. Use neutrals instead of coloring every word.

## Multi-state layouts (lobbies, matches, phases)

Modes with phases (lobby → countdown → match → final) need one layout per state, not one layout stretched across states. Keep a stable skeleton across all variants: same title, same anchor rows in the same positions, same footer. Swap only the state-specific rows (countdown ↔ timer ↔ result). Test the transition: a row that appears, disappears and reappears between states reads as flicker. If two states would differ by a single row, prefer one shared layout with a state word over two near-identical layouts.

## Small caps, with intent

Unicode small capitals such as `ᴘʟᴀʏ`, `ꜱᴛᴀᴛꜱ` and `ᴏɴʟɪɴᴇ` often make Latin metadata quieter and more compact. They are distinct codepoints with uneven coverage, widths and shapes; they are not semantic case transform. `SMALL CAPS` and `ꜱᴍᴀʟʟ ᴄᴀᴘꜱ` render differently. Compare at game scale. Leave Turkish labels (`Çevrimiçi`, `Bölge`, `Sıralama`) in ordinary letters unless a bundled font covers the whole word. Never substitute deceptive lookalikes for missing letters.

## Before and after: why

Cluttered survival sidebar:

```text
✦✦✦ ASTRA NETWORK ✦✦✦
☆ Welcome player ☆
●●● MONEY ●●● 1,250
◆◆ ONLINE ◆◆ 34
✦ STORE ✦ example.com ✦
```

More useful draft:

```text
ASTRA

Para       1.250
Bölge      Orman
Oyuncu     34

market.example
```

Whitespace groups values, Turkish labels remain recognizable, and only the title is prominent. This is a direction, not a fixed template; use match facts for PvP. A verified coin icon next to `Para` may help; icons on every row do not. TAB could use `ASTRA · Survival` and `34 oyuncu çevrimiçi` in the header, with `/yardım` in a quiet footer. Keep names and ranks in the actual list.

## Supplied visual references: CRAFTLUNA sidebars

View [first screenshot](../assets/reference-craftluna-1.png) and [second screenshot](../assets/reference-craftluna-2.png) only when a visual comparison is useful. These are actual in-game sidebar examples, not approved templates or evidence of TAB behavior.

| Observation | Transferable lesson | Check before reusing |
|---|---|---|
| Cyan server title, muted white labels, bright values | Make identity and values scannable without coloring every character | Test contrast on terrain, daylight and dark backgrounds |
| Small icons for crown, currency, death, region, vote and time | A coherent icon vocabulary can make distinct stats faster to locate | Confirm resource-pack glyphs or sprite support; provide text fallback |
| Blank space between identity/economy, local status and network status | Group by player question rather than adding ornamental separator rows | Keep related values together when a section grows |
| Date/time below title and domain at bottom | Stable framing may help a community server | Remove date/time or repeated domain if they do not serve a player need |
| Second screenshot places many colored values and timers in a narrow sidebar | Density can be warranted for progression, but competes with the game view | Test maximum value lengths, GUI scale, alignment and update jitter |

The images use Minecraft's pixel-like uppercase lettering. They do not demonstrate Unicode small caps. Do not label their typography as small caps or assume that the browser preview reproduces their exact font. The first groups town/kingdom and network status; the second emphasizes money, crystals, play time and a key timer. Learn from their information priorities, then select rows for the new server's own mode. Do not copy the server address, player name, colors or exact icon sequence by default.

## Score out of 10

Score each dimension 0, 1, or 2. Give concrete evidence for lost points. This is review guidance, not a universal taste claim.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Usefulness | Filler or wrong facts | Some useful facts, excess rows | Prominent rows help players |
| Hierarchy | No focal point/grouping | Partial grouping | Immediate priorities and groups |
| Restraint | Repeated ornaments/animation | Some needless effects | Decoration has a purpose |
| Legibility | Clipped, low contrast, cryptic | Readable with friction | Clear at game scale/narrow view |
| Compatibility | Unsupported feature assumed | Dependencies called out | Syntax, glyphs, fallbacks verified on target |

Interpret 0–2 poor, 3–4 passable, 5–6 promising, 7–8 good, 9–10 excellent. Without in-game verification, compatibility normally cannot receive 2. The preview's automated score is provisional: it counts length, symbols, dependencies and layout; it cannot judge whether a fact matters to that server.
