// Clean fixture for tools/lint_messages.py: must produce 0 findings.
package demo

object Chat {
    private val mm = MiniMessage.miniMessage()
    val prefix: Component = mm.deserialize("<gradient:#FFAA00:#FF5555>[Pazar]</gradient>")

    fun send(audience: Audience, body: Component) {
        audience.sendMessage(Component.text().append(prefix).append(Component.space()).append(body).build())
    }
}

class Messages(private val mm: MiniMessage) {
    fun sold(player: Player, buyer: String, amount: String) {
        val body = mm.deserialize("<gray>Sold to <buyer> for <amount></gray>",
            Placeholder.unparsed("buyer", buyer), Placeholder.unparsed("amount", amount))
        Chat.send(player, body)
    }

    val label = "ᴘᴀᴢᴀʀ"
    fun id(name: String) = name.lowercase(Locale.ROOT)
    fun display(name: String, loc: Locale) = name.uppercase(loc)
}
