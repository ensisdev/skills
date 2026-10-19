// Intentionally bad fixture for tools/lint_messages.py. Do not copy.
package demo

class Messages(private val mm: MiniMessage) {
    fun sold(player: Player, buyer: String, amount: Int) {
        player.sendMessage(mm.deserialize("<gray>Sold to " + buyer + " for " + amount))     // PREFIX-001, DATA-001
        player.sendMessage(Component.text("§aDone!"))                                         // PREFIX-001, COMPAT-001
    }

    val hand = "<gradient:#ff0000:#00ff00:#0000ff:#ffff00>[Pazar]</gradient> » Welcome"       // PREFIX-002, PREFIX-003 (4 stops)
    val other = "<gradient:#ffaa00:#ff5555>[Pazar]</gradient> ok"                             // PREFIX-003 (differs)
    val title = "✦ MARKET ✦"                                                                  // GLYPH-001
    val label = "ᴋıʟᴀᴠᴜᴢᴜ sᴀᴛış"                                                              // TR-001
    val upper = playerName.toUpperCase()                                                      // TR-002
    val col = "Name".padEnd(20)                                                               // DATA-002
}
