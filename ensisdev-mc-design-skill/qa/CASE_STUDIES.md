# CASE STUDIES — Caught Convergence, Redesigned

Worked examples of the anti-convergence engine applied. Each case shows the
convergent output (what an AI typically generates), the diagnosis via lint IDs,
and the redesign with recorded variation dimensions.

---

## Case 1 — Market main menu

### Before (convergent)
```
┌──────── 9x6 ────────────────┐
│ ✦ ✦ ✦ glass border ✦ ✦ ✦   │
│                             │
│        ✦ MARKET ✦           │
│   [item] [item] [item]      │
│   [item] [item] [item]      │
│                             │
│  ← glass    ✦ ✦ ✦    glass →│
└─────────────────────────────┘
```
**Diagnosis:** GLYPH-001 (paired title glyphs), GUI-001 (unjustified glass frame),
GUI-002 (corner arrows), VAR-001 (interchangeable with every other menu).
**Score vs neighbors:** 3/16.

### After — refs M01 + D01 (see EX-01)
```
ᴍᴀʀᴋᴇᴛ            Balance: 12,400c

▸ Diamond Sword      850c   14 left
▸ Iron Ingot x64     320c   82 left
…
[ Filter ]               page 2/7 →
```
**Varied dimensions:** composition (frame→list), title treatment (glyph-wrapped→small-cap label), icon strategy (decorative stars→semantic ▸), navigation placement (corner arrows→inline footer), density.
**After score:** 12/16.

---

## Case 2 — Prefix noise and uniform message bodies

### Before
```
[Market] » You bought a Diamond Sword.
[Market] » Not enough balance.
[Market] » Listing #142 sold!
[Market] » Invalid price.
```
(flat grey brackets, `»` separator, four identical body shapes)
**Diagnosis:** PREFIX-002 (separator glyph), PREFIX-003 (flat, hand-built), COPY-002 (error without recovery), uniform body shape.

### After — archetype split per intent (rules/TACTICAL_GUIDE.md §12)
```
[Pazar] ✓ Satın alındı: Diamond Sword — 867c.           ← result-first success
[Pazar] Bakiyen yetersiz. Gereken: 867c (eksik 120c).   ← problem + numbers
[Pazar] İlan #142 satıldı → 4,200c eklendi.             ← context-first notification
[Pazar] Fiyat 0 olamaz. Örnek: /market sell 500         ← guided recovery error
```
`[Pazar]` is the shared gradient prefix (one builder, brand gradient, no separator).
**Varied:** message architecture per intent, severity encoding beyond color,
copy specificity. Prefix stays constant; separator glyph removed and gradient applied.

---

## Case 3 — Universal three-line lore

### Before (every item)
```
• A powerful sword
(blank)
• Click to buy!
```
**Diagnosis:** LORE-001, LORE-003, COPY-001 ("Click to..." everywhere),
GLYPH-003 (uniform bullets).

### After — structure follows task (rules/TACTICAL_GUIDE.md §11)
- Commerce item → status/stock/action block (EX-14)
- Upgradeable tool → current/next/gate with delta (EX-15)
- Locked feature → reason + unlock path (EX-16)

**Varied:** lore schema per category, information order, whitespace rhythm.

---

## Case 4 — Small caps everywhere

### Before
```
ᴘʀᴏғɪʟᴇ ᴏꜰ ꜱᴛᴇᴠᴇ_ᴛʜᴇ_ʙᴜɪʟᴅᴇʀ_2004
ᴛᴏᴛᴀʟ ᴘʟᴀʏᴛɪᴍᴇ: 1,204 hours across 3 seasons of gameplay on this server
```
**Diagnosis:** TYPE-002, rule 001 violation (small caps on paragraphs and long
dynamic values), readability + localization harm.

### After
```
sᴛᴇᴠᴇ_ᴛʜᴇ_ʙᴜɪʟᴅᴇʀ_2004          ← name stays normal casing (rule 002)
Playtime: 1,204 hours (3 seasons) ← sentence case for data lines
```
Small caps retained ONLY for the two section labels. **Varied:** casing plan,
value emphasis, line length discipline.

---

## Scoring recap

| Case | Before | After | Key lever |
|---|---|---|---|
| 1 Market GUI | 3/16 | 12/16 | composition family |
| 2 Chat prefix | 2/16 | 13/16 | message archetypes |
| 3 Lore template | 4/16 | 11/16 | schema per task |
| 4 Small-caps flood | 5/16 | 12/16 | typography roles |

Run your own redesign through `DESIGN_REVIEW_TEMPLATE.md` and record it here-adjacent in the plugin repo.
