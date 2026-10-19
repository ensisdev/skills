# TURKISH COPY & TYPOGRAPHY — for Turkish-language Minecraft plugins

Applies when player-facing text is Turkish (or Turkish + English). Minecraft's default font renders `ç ğ ı İ ö ş ü` correctly; the problems below come from small caps, case conversion, number formatting and word endings.

---

## 1. Small caps and Turkish letters

Unicode has small-cap forms for most Latin letters (`ᴀ ʙ ᴄ ᴅ ᴇ ꜰ ɢ ʜ ɪ ᴊ ᴋ ʟ ᴍ ɴ ᴏ ᴘ ʀ s ᴛ ᴜ ᴠ ᴡ x ʏ ᴢ`; `s` and `x` have no distinct form) but **not** for `ç ğ ö ş ü`, and there is no separate small cap for dotless `ı`.

| Letter | Small-cap handling |
|---|---|
| `i` | `ɪ` |
| `ı` (dotless) | no dedicated glyph; keep normal `ı` (it sits at x-height and reads acceptably) — or avoid the word |
| `ç ğ ö ş ü` | **no small-cap form**; mixing a normal letter into a small-cap word looks broken (`sᴀᴛış`) |

Rules:
1. Small caps are only for labels whose words contain none of `ç ğ ö ş ü`. Good: `ᴘᴀᴢᴀʀ`, `ᴘᴏsᴛᴀ`, `ᴀʏᴀʀʟᴀʀ`, `ᴘʀᴏғɪʟ`, `ᴅᴜʀᴜᴍ`, `ᴛɪᴄᴀʀᴇᴛ`, `ʟɪsᴛᴇ`, `sᴇʀᴠᴇʀ`.
2. If the natural word has a special letter (`Satış`, `Güvenlik`, `Görev`, `Ödül`), use **normal case** for that label (and keep the typographic contrast with other cues: bold, color, spacing) or pick a synonym without the letter (`Görev` → `Kontrat`? only if it fits the product language).
3. Prefer a pack font with real small caps when a pack is guaranteed (`RESOURCE_PACK_UI.md` §5, code pattern §16); then the letter limitation disappears.
4. Check Bedrock rendering of small-cap glyphs (`BEDROCK_GEYSER.md`).

## 2. Case conversion: the İ/I trap (two opposite rules)

- **Display text** shown to a Turkish player: uppercase/lowercase with the Turkish locale (`i`→`İ`, `I`→`ı`): `text.toUpperCase(Locale.forLanguageTag("tr"))`. With `Locale.ROOT`, `"liste".toUpperCase()` gives `LISTE` where Turkish expects `LİSTE`.
- **Machine identifiers** (command names, permission nodes, config keys, material names, placeholders): always `Locale.ROOT` (or `Locale.ENGLISH`). With a Turkish default locale, `"TITLE".toLowerCase()` produces `tıtle` and breaks lookups. Never call no-arg `toLowerCase()`/`toUpperCase()` in plugin code.
- Prefer not to uppercase whole sentences at all; use the typographic hierarchy instead.

## 3. Numbers, currency, time

- Format with the player's locale (`player.locale()` on Paper) via `NumberFormat`/`DecimalFormat`: Turkish `12.400` and `12.400,50`, English `12,400` and `12,400.50`. One plugin must not mix both in the same screen.
- Currency stays attached to the number without a space only if the symbol/suffix is a single short token (`850c`, `₺850`); long names take a space (`850 altın`).
- Durations: `4:32` for clocks; words for long spans (`2 gün kaldı`). Use `sn`, `dk`, `sa`, `gün`.
- Dates: `17.10.2026` (day first). Never `10/17`.

## 4. Plurals and word endings

- After a numeral Turkish nouns stay singular: `3 ilan`, `12 eşya`, `5 dakika` — **not** `3 ilanlar`. Counted nouns need no plural logic.
- Dynamic suffixes are unsafe: `{oyuncu}'nın`, `{oyuncu}'a`. The correct suffix depends on the last vowel/consonant of an arbitrary name. Restructure instead of generating suffixes:
  - bad: `{oyuncu}'ın Tezgahı`
  - good: `Tezgah: {oyuncu}` · `Sahip: {oyuncu}`
- Static, known nouns may keep suffixes (`pazara`, `guild'e`) because you control the word.
- Use the apostrophe only for proper names; do not add it to common nouns.

## 5. Tone and voice

- Choose **sen** (direct, game-like, shorter) or **siz** (formal) per plugin and record it in `design-system.yml` (`tone: sen`). Do not mix.
- Imperatives for actions, bare stems: `Satın al`, `Vazgeç`, `Onayla`, `Geri dön`. Avoid `Lütfen ... tıklayınız` padding.
- Buttons name the effect: `Satın al · 867c`, `İptal et ve kapat`. Not `Tamam` / `Evet`.
- Errors: problem + next step: `Bakiyen yetersiz. Gereken: 867c (eksik 120c).`
- Keep English only for fixed technical terms players already know (`guild`, `kit`, `spawn`) and command names. Decide a glossary once (`guild` vs `lonca`; `market` vs `pazar`) and keep it in the design-system record.

## 6. Length and layout

- Turkish copy runs about 15–30% longer than English. Check GUI item names (they do not wrap), scoreboard lines (~28 visible characters), button labels in Dialogs.
- Lore wraps manually: break lines at ~30–35 characters; compound words are long, do not break inside words.
- Do not align columns with spaces (proportional font).

## 7. Glossary starter (edit per plugin)

| Concept | Short label | Longer form |
|---|---|---|
| Market | Pazar | Pazar yeri |
| Balance | Bakiye | Mevcut bakiye |
| Listing | İlan | Satış ilanı |
| Mailbox | Posta | Posta kutusu |
| Settings | Ayarlar | Oyuncu ayarları |
| Confirm | Onayla | Satın alımı onayla |
| Cancel | Vazgeç | İşlemi iptal et |
| Back | Geri | Önceki menü |
| Next / Previous | İleri / Geri | Sonraki / önceki sayfa |
| Locked | Kilitli | Henüz açılmadı |
| Cooldown | Bekleme | Bekleme süresi |

## 8. Checklist

- [ ] No small-cap label contains `ç ğ ö ş ü`
- [ ] No no-arg `toUpperCase()`/`toLowerCase()` in code; display uses `tr`, identifiers use `Locale.ROOT`
- [ ] Numbers/dates formatted per player locale
- [ ] No dynamic suffixes on player-supplied names
- [ ] `sen`/`siz` decided and recorded; glossary recorded
- [ ] Longest Turkish string fits item name / scoreboard / button width
