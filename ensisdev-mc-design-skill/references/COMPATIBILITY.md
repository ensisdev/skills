# COMPATIBILITY MATRIX — Design Decisions vs Platform Support

Design decisions must survive the lowest client/server version you support.
Verify against the project's actual target before implementing; this matrix is a
decision aid, not an API guarantee.

---

## 1. Feature support by client version

| Design feature | 1.8 | 1.12 | 1.13–1.15 | 1.16+ | Notes |
|---|---|---|---|---|---|
| Legacy colors (§0–§f) | ✅ | ✅ | ✅ | ✅ | universal baseline |
| Hex/RGB text colors | ❌ | ❌ | ❌ | ✅ | downgrades via nearest-legacy color |
| Gradients (per-char RGB) | ❌ | ❌ | ❌ | ✅ | collapses to solid on old clients |
| Bold / italic / underline | ✅ | ✅ | ✅ | ✅ | safe everywhere |
| Hover / click events | ✅ | ✅ | ✅ | ✅ | chat + items (GUIs: none) |
| Boss bar API | ⚠️ packets only | ✅ | ✅ | ✅ | 1.8 needs packet lib or BarAPI-style workaround |
| Action bar | ⚠️ packets | ✅ | ✅ | ✅ | legacy needs reflection/packets |
| Tab header/footer | ⚠️ packets | ✅ | ✅ | ✅ | |
| Custom fonts (resource pack) | ⚠️ partial | ⚠️ | ✅ | ✅ | glyph rendering varies by pack |
| TextDisplay entities | ❌ | ❌ | ❌ | ✅ 1.19.4+ | holograms on older = armor stands |

## 2. Unicode glyph rendering risks

Small-caps Latin letters (`ᴍᴀʀᴋᴇᴛ`) and common symbols render in the vanilla
default font, but risk increases with:

- custom client resource packs that replace `default` font glyphs
- translated strings containing characters outside Latin/Greek/Cyrillic blocks
- very new codepoints on very old clients

**Mitigation ladder** (apply per glyph, rule 110):

1. Prefer ASCII-safe alternatives for critical information (`!` instead of `⚠`)
2. Reserve decorative Unicode for surfaces where a fallback box is tolerable
3. Never let a glyph be the ONLY difference between two states
4. Test with the most popular PvP/PvE client packs, not just vanilla

## 3. MiniMessage & Adventure availability

- Paper 1.18+: bundled Adventure + MiniMessage natively.
- Spigot / older Paper: use `adventure-platform-*`; some features (gson-based
  hover on 1.8) degrade.
- If the plugin must run on non-Adventure platforms, keep the design system's
  message archetypes (result-first etc.) but implement via legacy serializers —
  the DESIGN survives, the syntax changes.

## 4. Graceful degradation rules

001. Design for the minimum supported version first; treat newer effects as enhancement.
002. Every gradient must have a defined single-color fallback.
003. Every hover-only detail must also exist in plain form somewhere reachable (rule: no hover-only information).
004. GUI slot layouts are version-stable (27/36/45/54) — never design against "future" inventory sizes.
005. Test the visual language at the lowest supported client with the worst-case resource pack.
006. Record the target version set in `design-system.yml` so later contributors do not silently break it.

## 5. Pre-release checklist

- [ ] Verified colors on min and max supported clients
- [ ] Glyph audit done against default font AND popular packs
- [ ] Bossbar/actionbar paths tested on legacy path (if 1.8 in scope)
- [ ] Fallbacks documented per feature in this file's copy inside the plugin repo

## 6. Modern clients (1.20.5 → 1.21.x)

Full detail: `MODERN_MC_FEATURES.md`. Summary of decision-relevant gates:

| Design feature | Min client | Fallback |
|---|---|---|
| Display-entity holograms | 1.19.4 | armor stands |
| Item data components (`item_name`, `tooltip_display`) | 1.20.5 / 1.21.5 | legacy name/flags |
| `item_model`, `tooltip_style` | 1.21.2 | base material + CMD |
| Text `shadow_color` / `<shadow>` (Adventure ≥ 4.18) | 1.21.4 | no shadow control |
| Native Dialogs | 1.21.6 | anvil / sign / chest GUI |
| Object text components, `<sprite>`/`<head>` (Adventure ≥ 4.25.0) | 1.21.9 | font glyph or ASCII icon |

Bedrock/Geyser gates: `BEDROCK_GEYSER.md`. Resource-pack-only gates: `RESOURCE_PACK_UI.md`.

