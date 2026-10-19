# EXAMPLES — Concrete Surface Design Examples

Each example shows a real composition decision. GUI examples are drawn on the real
9-column slot grid and tagged [vanilla] / [pack] / [dialog]; other surfaces use text mockups. Copy is shown in Turkish (primary) with some English; pick one language per plugin and follow `references/TURKISH_COPY.md` (small-caps letters, İ/I, plurals, suffixes). These are starting points to adapt, not templates to paste. Reference IDs
point into `references/REFERENCE_LIBRARY.md`.

---

## GUI Examples

**How to read these.** A chest GUI is a grid of 9 columns (c0–c8) × N rows (r0…). Each cell is one slot holding one item; the only text is the **title** (one line), **item names** and **lore**. There are no text columns, right alignment, buttons or panels. Every mockup below is drawn on that grid and tagged:

- **[vanilla]** — works with no resource pack, on Java and (via Geyser) Bedrock
- **[pack]** — needs a resource pack (`references/RESOURCE_PACK_UI.md`); always has a vanilla fallback described
- **[dialog]** — native Dialog (1.21.6+), see `references/MODERN_MC_FEATURES.md`

Legend: `·` empty slot · `LST` listing item (the real item with price in lore) · `◀ ▶` nav item · `ⓘ` info item · `✕` close item.

---

### EX-01 — Shop landing as price-first grid [vanilla]
**Refs:** M01 + D01 · **Task:** compare & buy fast · 4 rows, no filler panes
```
Title: ᴍᴀʀᴋᴇᴛ · 2/7
        c0  c1  c2  c3  c4  c5  c6  c7  c8
  r0    ·   ·   ·   ·   ⓘ   ·   ·   ·  FLT
  r1   LST LST LST LST LST LST LST LST LST
  r2   LST LST LST LST LST LST LST LST LST
  r3    ◀   ·   ·   ·   ·   ·   ·   ·   ▶
```
- `ⓘ` (r0c4): player head, name `Bakiye 12,400c`, lore = today's sales count. The balance lives in an item, not in the title.
- `LST`: the actual item. **Line 1 of lore is the price in bold** (`850c`), line 2 stock, line 3 seller; the item name stays the item's own name. Comparison happens by scanning lore line 1 down a column.
- `FLT` (r0c8): hopper-style filter item showing the active filter in its name.
- Sold-out listings: item replaced by `BARRIER`-style item named `Tükendi`, not a grayed-out void.
- Empty cells stay empty: grouping by whitespace, no glass-pane border.
- **[pack] variant:** same slots, a title glyph draws a price-column tint behind rows r1–r2; still no information only in the art.

### EX-02 — Settings: category rail in the grid [vanilla] → better as [dialog]
**Refs:** U02 · **Task:** configure without hunting · 6 rows
```
Title: Ayarlar · Bildirimler
        c0  c1  c2  c3  c4  c5  c6  c7  c8
  r0   GEN  ·  S01 S02 S03 S04 S05 S06  ·
  r1   MKT  ·  S07 S08 S09 S10 S11 S12  ·
  r2   MAIL ·   ·   ·   ·   ·   ·   ·   ·
  r3    ·   ·   ·   ·   ·   ·   ·   ·   ·
  r4    ·   ·   ·   ·   ·   ·   ·   ·   ·
  r5    ✕   ·   ·   ·   ·   ·   ·   ·   ·
```
- Column c0 = **category rail** (3 items: General / Market / Mail). The active category uses the glint override; its name starts with `▸` only if that glyph is renderable on the target platform.
- Cells c2–c7 = **settings**: each is one item whose *name is the setting* and whose *lore line 1 is the state in words* (`Açık` / `Kapalı`). State is also a different material (`LIME_DYE` vs `GRAY_DYE`) so it is not text-only or color-only.
- Column c1 is empty: whitespace separates rail from detail, no pane column.
- **Dialog alternative (1.21.6+):** a `multi_action` dialog with boolean toggles and a number-range slider is a better settings UI than a slot grid. Use the chest version only for pre-1.21.6 support.

### EX-03 — Mailbox: items first, groups by row [vanilla]
**Refs:** L04 + E02 · **Task:** claim what matters · 5 rows
```
Title: ᴘᴏsᴛᴀ · 4 yeni
        c0  c1  c2  c3  c4  c5  c6  c7  c8
  r0   TD  MAIL MAIL MAIL  ·   ·   ·   ·  ALL
  r1   YD  MAIL  ·   ·    ·   ·   ·   ·   ·
  r2    ·   ·    ·   ·    ·   ·   ·   ·   ·
  r3    ·   ·    ·   ·    ·   ·   ·   ·   ·
  r4    ◀   ·    ·   ·    ·   ·   ·   ·   ▶
```
- Each row begins with a **group header item** (`TD` = `Bugün (3)`, `YD` = `Dün (1)`); the mails of that group follow in the same row.
- `MAIL`: the mail's attachment item itself (or a `PAPER` for text mail); lore = sender, relative time, one verb (`Sol tık: al`).
- `ALL` (r0c8): `Hepsini al` — bulk action sits at the top, away from the pagination row.
- Claimed mails remain but use a muted material and `✓ Alındı` in lore.

### EX-04 — Confirmation as receipt, not celebration [vanilla] → better as [dialog]
**Refs:** A02 + M03 · **Task:** verify before commit · 3 rows
```
Title: Satın alma onayı
        c0  c1  c2  c3  c4  c5  c6  c7  c8
  r0    ·   ·   ·   ·  ITM  ·   ·   ·   ·
  r1    ·  NO   ·   ·  RCP  ·   ·   ·  YES
  r2    ·   ·   ·   ·   ·   ·   ·   ·   ·
```
- `ITM`: the product, unchanged.
- `RCP` (paper item), lore as a receipt: `Ürün 850c` / `Pazar vergisi (%2) 17c` / `Toplam 867c` / `Bakiye sonrası 11,533c`.
- `YES`: lime item `Satın al · 867c` (exact charge in the name). `NO`: red item `Vazgeç`. They sit at opposite ends (c1 / c8) so an accidental double-click does not hit both zones.
- No sparkles, no decorative border. Hover-free: everything is in the names/lore.
- **Dialog alternative:** `confirmation` dialog with body text as the receipt and two verb buttons.

### EX-05 — Empty state with next action [vanilla]
```
Title: ᴘᴀᴢᴀʀ
        c0  c1  c2  c3  c4  c5  c6  c7  c8
  r0    ·   ·   ·   ·   ·   ·   ·   ·   ·
  r1    ·   ·   ·  HOW  ·  CMD  ·   ·   ·
  r2    ·   ·   ·   ·   ·   ·   ·   ·   ·
```
- `HOW` (book): `Henüz ilan yok` — lore: "Satmak için elinde eşya tutup /market sell 500 yaz."
- `CMD` (command-block-style item): `Örnek göster` — suggests the command in chat.
Empty ≠ blank inventory. One explanation + one concrete command.

### EX-06 — Upgrade comparison [vanilla]
**Refs:** C01 · **Task:** decide between two tiers · 3 rows
```
Title: Yükseltme · Kılıç
        c0  c1  c2  c3  c4  c5  c6  c7  c8
  r0    ·  NOW  ·   ·   ARR  ·   ·  NXT  ·
  r1    ·  D1   ·   ·    ·   ·   ·  D2   ·
  r2    ·  S1   ·   ·   BUY  ·   ·  S2   ·
```
- `NOW` / `NXT`: the current and next-tier item (names `Şimdi` / `Seviye II`).
- `D1/D2` damage items, `S1/S2` speed items; each shows the number in its *name* (`Hasar 12` → `Hasar 18 (+%50)`). Unchanged stats read `Hız 8 (değişmez)` — never a fake improvement.
- `ARR` is a purely directional arrow item; `BUY` names the price: `Yükselt · 2,000c`.
- Two parallel columns make the comparison; the vertical alignment of D1/D2 is what lets the eye compare.

### EX-07 — Pagination footer variants [vanilla]
Rotate across the plugin's paginated screens; footer is always the **last row**, nav items are the only items in it:
```
variant A (explicit)   r5:  ◀   ·   ·   ·  3/9   ·   ·   ·   ▶
variant B (range)      r5:  ◀   ·   ·  "25–36 / 104"  ·   ·   ·  ▶
variant C (load-more)  r5:   ·   ·   ·   ·  MORE  ·   ·   ·   ·     ← MORE: "68 kaldı · devam"
```
Page count lives in an item name (`Sayfa 3/9`), not in the title, so the title can stay stable across pages.

---

## Chat Message Examples

All chat examples use the project's standard prefix: gradient `[Name]` (brackets inside the gradient), one space, body. Shown as plain text here; render with `Chat.send` (MINIMESSAGE_CODE_PATTERNS §18).

### EX-08 — Result-first success (transaction)
```
[Market] ✓ Sold 12× Diamond to Steve for 4,200c.
```
One line: gradient `[Market]` prefix, then result first with a semantic icon. Hover on the amount can show
the fee breakdown.

### EX-09 — Error with recovery instruction
```
[Pazar] Fiyat 0 olamaz. Örnek: /market sell 500
```
Problem + concrete next command. Never bare `Invalid argument.`

### EX-10 — Warning block with decision
```
[Pazar] ᴜʏᴀʀɪ — Son ilanınız 5 dakika içinde sona eriyor.
Uzat: /market extend 142
```
Small-caps severity label + context + action. Two lines maximum.

### EX-11 — Context-first notification (player may not remember trigger)
```
[Pazar] İlan #142 satıldı → 4,200c hesabına eklendi.
```
References the listing ID so history is traceable; no `Success!` wording.

### EX-12 — Onboarding first-run sequence (progressive, not a wall)
Message 1 (on join, once):
```
[Pazar] Yeni pazar sistemine hoş geldin. Elimdeki eşyayı
satmak için /market sell <fiyat> yazman yeterli.
```
Message 2 (only after first sale):
```
[Pazar] İlk satışını yaptın! Kazancın /market mailbox üzerinden teslim.
```
Each message unlocks the next concept; nothing dumps all commands at once.

### EX-13 — Cooldown reminder (compact)
```
[Pazar] ⌛ Pazar vergisi 30 sn sonra sıfırlanacak.
```

## Lore Examples

### EX-14 — Commerce lore (identity → state → action)
```
Diamond Sword
Eşsiz hasar, standart dayanıklılık.

Satışta · 850c            ← status + price as data
Stok: 14
Sol tıkla satın al
```

### EX-15 — Upgradeable tool lore (current → next → gate)
```
Kazma Ustası III
Blok başına +%25 şans ek drop için.

Sonraki seviye: +%40          ← delta, not restated stats
Gereken: 500 cevher kazısı    ← requirement near its gate
```

### EX-16 — Locked feature lore (feature → reason → unlock path)
```
Kilitli — Guild Deposu
Bu alan yalnızca guild üyeleri için açık.

Bir guild'e katıl veya /guild create ile kur.
```

### EX-17 — Reward claim lore (reward → condition → claim state)
```
Haftalık Ödül #33
2,000c + 1 Anahtar

✓ Alındı — Perşembe 00:00'da yenilenir.
```

## Transient Surface Examples

### EX-18 — Action bar (one value + one hint)
```
⌛ İlan süresi 4:32  ·  uzatmak için /market extend 142
```

### EX-19 — Boss bar (event phases change color, copy stays stable)
```
Çift XP Hafta Sonu  ▐▐▐▐▐▐▐░░░  2 gün kaldı
```
Phase changes recolor the bar and swap one word (`başladı / bitti`), never the layout.

### EX-20 — Scoreboard sections with whitespace grouping
```
ᴘᴀᴢᴀʀ
Bakiye      12,400c
İlanlar           3

sᴇʀᴠᴇʀ
Online           148
Ping             23ms
```
Labels left, values right-aligned, blank line between sections. No glyph separators.

### EX-21 — Tablist header/footer (compact brand + utility header)
```
HEADER:  ᴡᴀʀᴢᴏɴᴇ · sezon 4   |   /market /help /guild
FOOTER:  discord.sunucu.gg
```
Header carries navigation value; footer only identity. No ASCII art walls.

### EX-22 — Hologram above shop chest (glanceable)
```
Steve'in Tezgahı
14 ürün · bugün 8 satış
```
Two lines max. Status lives in the world where the decision happens.

---

## Dialog & Book Examples

### EX-23 — Confirmation dialog (one question, two contrasting answers)
**Refs:** W02 · **Task:** prevent irreversible mistake
```
Başlık:  Tezgahı kapat
Gövde:   2 aktif ilanınız iptal olur ve
         alıcılar iade edilir.
Buton:   [ İptal et ve kapat ]   [ Vazgeç ]
```
Consequence sentence before the buttons; destructive option named explicitly.

### EX-24 — NPC dialog (context-first, one beat per screen)
```
ᴛɪᴄᴀʀᴇᴛ · ᴏʀʜᴀɴ
"Bugün elmas arayan çoktu. Elinde varsa
kazancın garanti."
[ Satılık listesi ]   [ Ayrıl ]
```
Dialog advances one idea at a time; choices are verbs in world-voice, not `OK/Cancel`.

### EX-25 — Book guide (chaptered with TOC)
```
Page 1 (TOC):
ᴘᴀᴢᴀʀ ᴋıʟᴀᴠᴜᴢᴜ
1. Satış ………… sayfa 2
2. Alım  ………… sayfa 3
3. Güvenlik …… sayfa 4

Page 2:
1 · Satış
Elindeki eşya ile /market sell <fiyat>.
Vergi %2'dir ve alıcıdan kesilmez.
→ devam: sayfa 3
```

## Anti-convergence checklist for every new example you build

- [ ] Composition differs from the nearest 3 screens in ≥3 dimensions
- [ ] Title treatment not reused verbatim from a sibling screen
- [ ] At most 0–2 decorative glyphs per cluster; all icons semantic
- [ ] Success/error distinguishable without color alone
- [ ] Empty/disabled/locked states designed with next-action copy
- [ ] Long player names and translated strings tested for layout breakage
- [ ] Dynamic values use unparsed placeholders (never raw markup injection)
- [ ] Reference IDs recorded: borrowed / changed / why

## Reference seed index

| Example | Seeds |
|---|---|
| EX-01 shop landing | M01, D01 |
| EX-02 settings rail | U02 |
| EX-03 mailbox | L04, E02 |
| EX-04 confirmation | A02, M03 |
| EX-05 empty state | U01 |
| EX-06 upgrade compare | C01 |
| EX-08–13 chat set | rules/TACTICAL_GUIDE.md §12 archetypes |
| EX-14–17 lore set | rules/TACTICAL_GUIDE.md §11 patterns |
| EX-19 boss bar | S03 |
| EX-20 scoreboard | E02 |
| EX-22 hologram | S01 |
| EX-23 dialog | W02 |
| EX-24 NPC dialog | E04 |
| EX-25 book guide | E03 |

---

## Additional Surface Examples

### EX-26 — Advancement-style toast (passive notification)
```
┌──────────────────────────────┐
│ ▫  İlanın satıldı            │
│    Diamond Sword · 4,200c    │
└──────────────────────────────┘
   (auto-dismiss 5 sn, ses: confirm)
```
One title + one detail line. Never duplicates the same content into chat — pick one surface per event. Sound cue carries the "something happened" signal.

### EX-27 — Shop sign (world-anchored micro UI)
```
Line 1:  [ᴘᴀᴢᴀʀ]
Line 2:  Diamond ×1
Line 3:  850c
Line 4:  Steve
```
Status first, ≤4 short lines, no decoration. Click opens the full listing GUI — the sign advertises, the GUI transacts.

### EX-28 — Map canvas overview (territory/economy map)
```
Legend (fixed corner):
■ guild lands   □ free   ✕ contested
Palette: 3 fills max; borders only for contested zones.
```
Legend precedes decoration; every fill color maps to exactly one meaning. No pixel-art flourish that competes with data.



