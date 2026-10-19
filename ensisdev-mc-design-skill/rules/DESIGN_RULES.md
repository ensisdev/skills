# DESIGN RULES — 110 CORE NORMATIVE RULES

These rules are normative. An AI agent should treat them as defaults and document any deliberate exception.

> This is the deduplicated core of the original 300-rule corpus. The expanded per-surface variants
> (`DESIGN_RULES_300.md`) apply these same rules to specific surface types; consult it only when
> working on an unusual surface. In practice, applying the 110 core rules covers all cases.

## Typography & casing
001. Use small caps only for short labels, not paragraphs.
002. Keep player names in normal casing unless the product identity explicitly requires another treatment.
003. Use one primary heading treatment per screen family.
004. Do not fake small caps with random Unicode characters when real font support is unavailable.
005. Use bold/weight to establish hierarchy before adding decorative glyphs.
006. Do not use full uppercase for every GUI title.
007. Keep dynamic numeric values visually distinct from descriptive text.
008. Use sentence case for instructions when readability matters more than branding.
009. Use compact uppercase or small caps for metadata only when the line is short.
010. Keep action verbs visually prominent in interactive labels.

## Iconography & glyphs
011. Each icon must communicate object, action, state, or category.
012. Avoid using the same sparkle glyph on more than one semantic role.
013. Do not surround every title with decorative symbols.
014. Prefer meaningful Minecraft item icons when they improve recognition.
015. Set a decorative glyph budget for each surface.
016. Use one directional symbol consistently within a navigation family.
017. Do not use arrows as decoration when no action or direction exists.
018. Avoid mixing unrelated icon families on one screen.
019. Use icon repetition to show status only when the meaning is stable.
020. Remove an icon that adds no semantic information.

## GUI composition
021. Do not default every feature to a 9x6 chest.
022. Choose slot geometry from task priority, not habit.
023. Give the primary action a predictable location within a screen family.
024. Reserve navigation space only when navigation is actually needed.
025. Avoid decorative filler slots when content is already dense.
026. Use grouping to separate categories before adding borders.
027. Do not use glass panes as a universal frame.
028. Keep detail views visually distinct from collection views.
029. Use pagination only when content cannot be made scannable another way.
030. Do not put every button on the bottom row by default.

## Information architecture
031. Place the most decision-relevant information first.
032. Group data by user task, not by implementation class.
033. Separate discovery from action when the choice is complex.
034. Use progressive disclosure for advanced controls.
035. Avoid showing every available action at equal emphasis.
036. Make status and consequences obvious before destructive actions.
037. Keep comparison views aligned across comparable items.
038. Use consistent labels for the same concept across the plugin.
039. Do not duplicate the same state in multiple visual treatments unless needed.
040. Use empty states to explain what the player can do next.

## Messages
041. Every chat message starts with the plugin's gradient `[PluginName]` prefix; do not add separator glyphs after it and do not vary the prefix per message.
042. Put the result first for simple transactional messages.
043. Put the next action first when recovery is needed.
044. Use compact messages for repeated low-risk feedback.
045. Use structured messages for warnings that require a decision.
046. Avoid unnecessary punctuation as a substitute for hierarchy.
047. Do not make success/error distinguishable only by color.
048. Keep chat messages readable without hover effects.
049. Use context-first messages when players may not remember the triggering action.
050. Do not repeat the full command syntax when a concise action label is enough.

## Item names & lore
051. Make an item name identify the object before adding personality.
052. Do not use the same three-line lore structure for every item.
053. Keep mechanics separate from flavor when both are present.
054. Use section labels only when they improve scanning.
055. Keep action instructions explicit.
056. Put requirements near the action they gate.

057. Use aligned comparisons for upgrade or marketplace screens.
058. Avoid lore that repeats information already shown by the item name.
059. Keep dynamic values visually stable across similar items.
060. Do not hide important restrictions in flavor text.

## Color semantics
061. Assign colors semantic roles instead of choosing them line by line.
062. Do not use green for unrelated decorative accents everywhere.
063. Keep warning and destructive semantics consistent across surfaces.
064. Use neutral text for neutral information.
065. Avoid encoding a required distinction only by color.
066. Do not create a rainbow hierarchy with no semantic purpose.
067. Reserve accent color for interactive or brand-critical elements.
068. Use muted tones to reduce visual competition between secondary metadata.
069. Keep disabled states distinguishable without erasing legibility.
070. Do not change a status color arbitrarily between GUI and chat.

## Spacing & density
071. Use spacing to create groups before adding decorative borders.
072. Avoid filling every blank slot or line.
073. Use consistent rhythm within a component family.
074. Let high-priority information breathe.
075. Increase separation before adding another glyph.
076. Keep repeated list rows aligned.
077. Avoid dense walls of lore text when a concise label can replace them.
078. Use compact layouts only for genuinely high-frequency workflows.
079. Do not compress all controls merely to fit one more option.
080. Preserve a visual pause before destructive actions.

## Interaction & states
081. Design default, hover, click, disabled, empty, loading, success, and error states when applicable.
082. Do not make an action discoverable only through a decorative icon.
083. Keep confirmation actions clearly distinct from cancel actions.
084. Show current selection without relying on a single tiny marker.
085. Use progress feedback for actions that may take noticeable time.
086. Do not promise an action in lore that the click handler cannot perform.
087. Ensure unavailable actions explain why they are unavailable when useful.
088. Keep back/navigation behavior predictable within a feature family.
089. Avoid accidental destructive clicks by separating them from default actions.
090. Use hover details to augment, not replace, essential information.

## Localization & content
091. Design for longer translated strings.
092. Do not depend on English word length for alignment.
093. Keep placeholders semantically named.
094. Avoid embedding language-specific punctuation into reusable layout logic.
095. Do not build a visual hierarchy that collapses when a name becomes long.
096. Keep numeric formats locale-aware where the platform supports it.
097. Use consistent terminology for the same gameplay concept.
098. Do not abbreviate uncommon terms purely to save space.
099. Make pluralization and count wording adaptable.
100. Do not expose raw placeholder keys to players.

## Anti-patterns & review
101. Reject a redesign that changes only colors.
102. Reject a redesign that changes only glyphs.
103. Reject a redesign that changes only the title.
104. Compare new surfaces to at least three neighboring screens.
105. Record intentional exceptions to the rule set.
106. Prefer semantic variation over arbitrary visual novelty.
107. Do not add visual noise just to appear different.
108. Use a plugin-level design system record to preserve coherence.
109. Run a final copy/readability pass separately from a style pass.
110. Review unusual Unicode before shipping it.

