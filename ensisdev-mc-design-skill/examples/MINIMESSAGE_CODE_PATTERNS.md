# MINIMESSAGE CODE PATTERNS — Implementation Reference

Concrete Paper/Adventure patterns for the design decisions in this skill.
Target: Paper 1.20+ with Adventure API. Verify against your project's versions.

---

## 1. Semantic palette as single source of truth

Define roles once; never pick colors per line. This implements rules/TACTICAL_GUIDE.md §20.

```kotlin
object Theme {
    val brand    = NamedTextColor.GOLD
    // gradient stops for the chat prefix (see section 18)
    const val PREFIX_FROM = "#FFAA00"
    const val PREFIX_TO   = "#FF5555"
    val accent   = NamedTextColor.YELLOW
    val text     = NamedTextColor.GRAY
    val muted    = TextColor.fromHexString("#8a8a8a")!!
    val success  = NamedTextColor.GREEN
    val warning  = NamedTextColor.YELLOW
    val danger   = NamedTextColor.RED
    val value    = NamedTextColor.WHITE   // dynamic numerals

    // Small caps only for short labels (rule 001)
    const val LABEL_MARKET = "ᴍᴀʀᴋᴇᴛ"
    const val LABEL_STATUS = "ᴅᴜʀᴜᴍ"
}
```

## 2. Result-first success message with hover detail

```kotlin
fun saleSuccess(item: String, amount: Int, buyer: String, fee: Int): Component =
    Component.text()
        .append(Component.text("✓ ", NamedTextColor.GREEN))
        .append(Component.text("Satıldı: ", Theme.text))
        .append(Component.text("$amount c", Theme.value))
        .append(Component.text(" → $buyer", Theme.text))
        .hoverEvent(HoverEvent.showText(
            Component.text("Komisyon: $fee c", Theme.muted)
        ))
        .build()
```
Note: `item` and `buyer` are player-influenced strings — see pattern 7 before
inserting them anywhere near markup.

## 3. Error with recovery command (clickable)

```kotlin
fun invalidPrice(given: String): Component =
    Component.text()
        .append(Component.text("Fiyat geçersiz: ", Theme.danger))
        .append(Component.text(given, Theme.value))
        .append(Component.newline())
        .append(Component.text("Örnek: ", Theme.text))
        .append(
            Component.text("/market sell 500", Theme.accent)
                .clickEvent(ClickEvent.suggestCommand("/market sell "))
                .hoverEvent(HoverEvent.showText(
                    Component.text("Komutu yazmaya başla", Theme.muted)
                ))
        )
        .build()
```

## 4. Safe dynamic values: unparsed placeholders

User text must never be parsed as MiniMessage markup (lint rule DATA-001).

```java
// SAFE: user input enters as placeholder value
Component msg = MiniMessage.miniMessage().deserialize(
    "<gray>Satıcı:</gray> <white><seller></white>",
    Placeholder.unparsed("seller", sellerName)
);

// UNSAFE — never do this:
// MiniMessage.miniMessage().deserialize("<gray>Satıcı:</gray> " + sellerName);
```
Use `Placeholder.component()` only when you deliberately allow rich content
from a trusted source.

## 5. Small-caps label + normal title hierarchy (GUI title)

```kotlin
fun guiTitle(section: String): Component =
    Component.text()
        .append(Component.text("ᴍᴀʀᴋᴇᴛ ", Theme.brand))
        .append(Component.text("· ", Theme.muted))
        .append(Component.text(section, NamedTextColor.WHITE))
        .build()
```

---

## 6. Lore builder with task-based structure

Implements rules/TACTICAL_GUIDE.md §11 — structure chosen per item category, never one template.

```kotlin
fun commerceLore(status: String, price: Int, stock: Int): List<Component> = listOf(
    Component.empty(),                                        // whitespace as grouping
    Component.text("$status · ", Theme.muted)
        .append(Component.text("$price c", Theme.value)),
    Component.text("Stok: ", Theme.text)
        .append(Component.text(stock.toString(), Theme.value)),
    Component.text("Sol tıkla satın al", Theme.accent)
)

fun lockedLore(requirement: String, unlockPath: String): List<Component> = listOf(
    Component.text("Kilitli", Theme.danger),
    Component.text("Gereken: $requirement", Theme.text),
    Component.empty(),
    Component.text(unlockPath, Theme.accent)
)
```

## 7. Localized, pluralization-safe messages

Implements rules 091–099: never build sentences by string concatenation.

```yaml
# messages_tr.yml
sale_success:
  one: "✓ Eşyan satıldı: <amount> c"
  other: "✓ <count> eşyan satıldı: toplam <amount> c"
```

```kotlin
fun saleMessage(count: Int, amount: Int): Component {
    val key = if (count == 1) "sale_success.one" else "sale_success.other"
    return MiniMessage.miniMessage().deserialize(
        messages[key]!!,
        Placeholder.unparsed("count", count.toString()),
        Placeholder.unparsed("amount", amount.toString())
    )
}
```

## 8. Action bar (transient: one value + one hint)

```kotlin
fun listingTimer(secondsLeft: Long, listingId: Int): Component =
    Component.text()
        .append(Component.text("⌛ ", Theme.warning))
        .append(Component.text(formatMmSs(secondsLeft), Theme.value))
        .append(Component.text("  ·  ", Theme.muted))
        .append(Component.text("/market extend $listingId", Theme.text))
        .build()

player.sendActionBar(listingTimer(272, 142))
```
Update at most 2×/second; do not spam the packet channel.

## 9. Boss bar with phase semantics

```kotlin
val eventBar = BossBar.bossBar(
    Component.text("Çift XP Hafta Sonu", NamedTextColor.AQUA),
    0.75f,
    BossBar.Color.BLUE,
    BossBar.Overlay.PROGRESS
)

// Phase change: recolor + swap ONE word; layout stays stable (EX-19)
fun setPhase(bar: BossBar, live: Boolean) {
    bar.color(if (live) BossBar.Color.GREEN else BossBar.Color.BLUE)
}
```

---

## 10. Scoreboard with whitespace grouping (EX-20)

```kotlin
fun scoreboardLines(balance: Int, listings: Int, online: Int): List<Component> = listOf(
    Component.text("ᴘᴀᴢᴀʀ", Theme.brand),
    row("Bakiye", "$balance c"),
    row("İlanlar", "$listings"),
    Component.empty(),                     // section break, not a glyph separator
    Component.text("sᴇʀᴠᴇʀ", Theme.brand),
    row("Online", "$online")
)

private fun row(label: String, value: String): Component =
    Component.text()
        .append(Component.text(label.padEnd(10), Theme.text))
        .append(Component.text(value, Theme.value))
        .build()
```
Note: `padEnd` assumes monospace rendering of the default font for Latin text;
re-verify alignment per locale (rule 092).

## 11. Pagination footer variants

Rotate across surfaces so no two screens share one footer (EX-07).

```kotlin
fun explicitFooter(page: Int, pages: Int): Component = ...   // ‹ prev  page 3/9  next ›
fun rangeFooter(from: Int, to: Int, total: Int): Component = // ◀ ▶  showing 25–36 of 104
fun loadMoreFooter(remaining: Int): Component =              // more below ↓ (68 remaining)
```

## 12. Pre-ship safety checklist (code side)

- [ ] All user-derived strings enter via `Placeholder.unparsed(...)` — never raw concatenation into markup
- [ ] No hover-only information; everything readable without hovering
- [ ] State not encoded by color alone (word/icon accompanies it)
- [ ] Action bar/bossbar updates rate-limited
- [ ] Unicode glyphs verified in the target Minecraft version's font (rules 004, 110)
- [ ] Strings externalized for translation; no hardcoded sentence assembly
- [ ] Click commands use `suggestCommand` for destructive or multi-arg actions
- [ ] Long values tested: 16-char names, 7-digit balances, translated labels

## 13. Design-system record template

Keep this in the plugin repo so coherence survives contributors (rule 108):

```yaml
# design-system.yml
palette:
  brand: "#FFAA00"
  success: "#55FF55"
  danger: "#FF5555"
  muted: "#8A8A8A"
typography:
  gui_titles: "small-caps label + normal section name"
  chat_prefix: "<gradient:#FFAA00:#FF5555>[Pazar]</gradient>"
  chat_success: "prefix + result-first, ✓ icon"
  chat_error: "problem + recovery command"
surfaces:
  market_main: { refs: [M01, D01], footer: "range" }
  settings:    { refs: [U02], footer: null }
sounds:
  confirm: { key: "minecraft:entity.experience_orb_pickup", pitch: 1.4, volume: 0.6 }
  deny:    { key: "minecraft:entity.villager.no", pitch: 0.8, volume: 0.7 }
```

---

## 14. Inventory GUI skeleton (holder pattern + slot→action mapping)

```kotlin
class GuildBankMenu(
    private val player: Player,
    private val bank: GuildBank
) : InventoryHolder {
    private lateinit var inventory: Inventory
    private val actions = mutableMapOf<Int, () -> Unit>()   // slot -> behavior

    override fun getInventory(): Inventory = inventory

    fun open() {
        inventory = Bukkit.createInventory(this, 54, guiTitle("Depo"))
        render()
        player.openInventory(inventory)
        Sound.play(player, Theme.Sounds.open)   // see §15
    }

    /** Targeted refresh — never clear()+refill (see PERFORMANCE_NOTES §1). */
    fun updateSlot(slot: Int, stack: ItemStack) {
        if (inventory.getItem(slot)?.isSimilar(stack) != true) {
            inventory.setItem(slot, stack)
        }
    }

    fun handleClick(slot: Int, click: ClickType): Boolean {
        val action = actions[slot] ?: return false   // pass-through slots stay native
        action()
        return true                                  // cancel vanilla item movement only on action slots
    }

    private fun render() {
        // rail: roles; content: items with per-slot actions
    }
}
```
Listener side maps `InventoryClickEvent.view.holder as? GuildBankMenu` →
`handleClick(event.slot, event.click)`. One listener class serves all menus that
implement this contract.

## 15. Semantic sound playback

```kotlin
object SoundUx {
    enum class Role(val key: String, val pitch: Float, val volume: Float) {
        CONFIRM("entity.experience_orb_pickup", 1.4f, 0.6f),
        DENY("entity.villager.no", 0.8f, 0.7f),
        OPEN("block.chest.open", 1.0f, 0.6f);
        // one role = one sound (SOUND_UX rule 001); extend via design-system.yml
    }

    private val lastPlayed = mutableMapOf<UUID, MutableMap<Role, Long>>()

    fun play(p: Player, role: Role) {
        val now = System.currentTimeMillis()
        val prev = lastPlayed.getOrPut(p.uniqueId){ mutableMapOf() }[role] ?: 0
        if (now - prev < 1000) return          // rate limit identical cues (rule 003)
        lastPlayed[p.uniqueId]!![role] = now
        p.playSound(p.location, role.key, Sound.Source.UI, role.volume, role.pitch)
    }
}
```

## 16. Real small caps via resource-pack font

When a controlled resource pack exists, prefer a real small-caps FONT over Unicode
lookalikes (rules 004 + COMPATIBILITY §2):

```kotlin
// Pack defines 'market:smallcaps' mapping lowercase→small-cap glyphs.
// MiniMessage switches fonts inline:
val title = MiniMessage.miniMessage().deserialize(
    "<font:market:smallcaps>Market</font> <gray>·</gray> <white>Depo</white>"
)
```
- Ship an ASCII-fallback check: if the pack is absent, the text still reads as
  normal letters ("Market") — graceful degradation by construction.
- Keep the Unicode-lookalike variant behind a config flag for pack-less servers.

## 17. Toast-style notification via advancement trigger (1.20+)

```kotlin
// Fire-and-forget toast without granting a visible advancement:
val adv = Advancement.builder()
    .display(
        ItemStack.of(Material.DIAMOND),
        Component.text("İlanın satıldı", NamedTextColor.WHITE),       // EX-26 title
        Component.text("Diamond Sword · 4,200c", Theme.text),         // one detail line
        FrameType.TASK, true, true, false)
    .build()
// register hidden advancement, grant, then revoke on next tick
```
Rate-limit toasts like sounds; never mirror the same event into chat too (EX-26 note).

## 18. Standard chat prefix — gradient `[PluginName]`

Project rule: every chat message starts with the same gradient bracketed plugin name, one space, then the body. Build it once.

```kotlin
object Chat {
    private val mm = MiniMessage.miniMessage()
    private const val NAME = "Pazar"

    // Components are immutable; render once and reuse.
    val prefix: Component = mm.deserialize(
        "<gradient:${Theme.PREFIX_FROM}:${Theme.PREFIX_TO}>[$NAME]</gradient>"
    )

    // Single-color fallback for paths without hex/gradient support.
    val prefixFallback: Component = Component.text("[$NAME]", Theme.brand)

    /** Every outgoing chat message goes through here. */
    fun send(audience: Audience, body: Component, legacy: Boolean = false) {
        audience.sendMessage(
            Component.text()
                .append(if (legacy) prefixFallback else prefix)
                .append(Component.space())     // a space is the only separator
                .append(body)
                .build()
        )
    }
}

// usage: the body keeps its own architecture (result-first here)
Chat.send(player, saleSuccess("Diamond Sword", 12, "Steve", 85))
```

- Brackets inside the gradient; 2 stops, 3 max; same stops everywhere.
- No `»`, `>>`, `|` after the prefix; a plain space only.
- Multi-line messages: prefix on the first line only.
- Not used for action bar, bossbar, titles, GUI, lore, scoreboard.
- The prefix string is trusted; player text goes only into the body via `Placeholder.unparsed`.
- Lint: PREFIX-001..004.

## 19. Localized messages (tr/en) with the standard prefix

Message files hold **bodies only**; the prefix is added by `Chat.send` (§18). Keys are stable identifiers; copy lives in `messages_<lang>.yml`.

```yaml
# messages_tr.yml
sale.success: "<green>✓</green> <gray>Satıldı:</gray> <white><amount>c</white> <gray>→ <buyer></gray>"
price.invalid: "<gray>Fiyat 0 olamaz. Örnek:</gray> <white>/market sell 500</white>"
# messages_en.yml
sale.success: "<green>✓</green> <gray>Sold:</gray> <white><amount>c</white> <gray>→ <buyer></gray>"
price.invalid: "<gray>Price can't be 0. Example:</gray> <white>/market sell 500</white>"
```

```kotlin
object Lang {
    private val mm = MiniMessage.miniMessage()
    private val bundles = mutableMapOf<String, Map<String, String>>()   // "tr" -> key -> raw
    private const val FALLBACK = "en"

    fun load(lang: String, map: Map<String, String>) { bundles[lang] = map }

    private fun raw(player: Player, key: String): String {
        val lang = player.locale().language                       // "tr", "en", ...
        return bundles[lang]?.get(key) ?: bundles[FALLBACK]?.get(key) ?: key
    }

    fun body(player: Player, key: String, vararg r: TagResolver): Component =
        mm.deserialize(raw(player, key), TagResolver.resolver(*r))

    fun send(player: Player, key: String, vararg r: TagResolver) =
        Chat.send(player, body(player, key, *r))
}

// usage: player text goes through unparsed placeholders only
Lang.send(player, "sale.success",
    Placeholder.unparsed("amount", numberFormat(player).format(4200)),
    Placeholder.unparsed("buyer", buyerName))

// locale-aware numbers (Turkish 4.200 vs English 4,200)
fun numberFormat(p: Player): NumberFormat = NumberFormat.getInstance(p.locale())
```

- Missing key falls back to English, then to the key itself (visible in testing, never an exception).
- Case conversion for display uses the player's locale; identifiers use `Locale.ROOT` (see `references/TURKISH_COPY.md` §2).
- No dynamic suffixes on names (`<buyer>'a`); restructure the sentence.
- Do not store the prefix in message files; one source of truth (§18).

