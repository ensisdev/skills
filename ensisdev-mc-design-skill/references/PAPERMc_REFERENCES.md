# ensisdev-mc-design — Platform & Design References

These are implementation references for AI coding agents. They should inform what is technically possible; they are not visual templates to copy.

## 1. Paper / Adventure overview

Paper documents Adventure as the text/component system used across many player-facing surfaces, including text, boss bars, titles, books, tab lists, localization and resource packs.

Reference:
https://docs.papermc.io/adventure/

Design implication:
Do not assume every player-facing UI is a raw string. Treat structured components as a design tool.

## 2. Adventure Text Components

Reference:
https://docs.papermc.io/adventure/text/

Important capabilities:
- component trees
- parent/child styles
- RGB colors
- text decorations
- hover events
- click events
- translation components
- keybind components
- serialization

Design implication:
Use hierarchy in the component tree instead of simulating hierarchy with repeated Unicode punctuation.

## 3. Paper Component API

Reference:
https://docs.papermc.io/paper/dev/component-api/introduction/

Design implication:
Use structured components for user-facing output where the platform supports them. Components allow richer styling and interaction than legacy flat strings.

## 4. MiniMessage overview

Reference:
https://docs.papermc.io/adventure/minimessage/

Design implication:
MiniMessage can represent complex text components in a readable configuration-oriented format. Keep style semantics meaningful instead of nesting decorative formatting everywhere.

## 5. MiniMessage format

Reference:
https://docs.papermc.io/adventure/minimessage/format/

Relevant capabilities:
- colors
- hover events
- click events
- insertion
- custom fonts
- newline handling
- translation
- score/NBT-related component output

Design implication:
Hover and click can expose secondary information without cluttering the primary message. Custom fonts can be used deliberately when the resource-pack environment is controlled.

## 6. MiniMessage dynamic replacements

Reference:
https://docs.papermc.io/adventure/minimessage/dynamic-replacements/

Design implication:
Use component and unparsed placeholders for dynamic/user-provided values. Do not accidentally treat untrusted dynamic content as formatting markup.

## 7. MiniMessage API

Reference:
https://docs.papermc.io/adventure/minimessage/api/

Design implication:
Centralizing parsing/tag behavior can make a plugin's visual language easier to manage consistently.

## 8. Localization / translation

Adventure documentation includes translation support and MiniMessage translation tooling.

Reference:
https://docs.papermc.io/adventure/minimessage/translator/

Design implication:
A design should survive localization. Never depend on exact English string widths for alignment.

## 9. Current-platform reminder

These references were checked against current Paper documentation in August 2026. Platform APIs can change, so verify version-specific API details against the project's target Paper/Adventure version before implementation.

The skill is about **design principles**, not about freezing a particular API version.

## 10. Sources used to verify MODERN_MC_FEATURES.md (October 2026)

- Paper Dialog API Javadoc (`@Experimental`, present in 1.21.8 and later): https://jd.papermc.io/paper/1.21.8/io/papermc/paper/dialog/Dialog.html
- Adventure version history (4.18 shadow color support on 2024-12-22; 4.25.0 object component serialization + head tag on 2026-04-16; 4.24.0 close-dialog method): https://docs.papermc.io/adventure/version-history/adventure/
- MiniMessage format (shadow, sprite and head tags): https://docs.papermc.io/adventure/minimessage/format/
- Scoreboard number formats (snapshot 23w46a, 1.20.3): https://minecraft.net/en-us/article/minecraft-snapshot-23w46a
- `tooltip_display` (record with hide-tooltip flag and hidden component set; 1.21.5 data fixer): https://mappings.dev/1.21.6/net/minecraft/world/item/component/TooltipDisplay.html
- Object text components in 1.21.9 (secondary source, mod author notes; not Mojang's changelog): https://modrinth.com/project/Wb5oqrBJ/version/F4hhFg88

