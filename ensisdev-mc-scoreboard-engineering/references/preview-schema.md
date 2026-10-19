# Preview input

Pass UTF-8 JSON to `scripts/preview.py`. Strings are plain text. For styling, use explicit `segments` with `color`, `bold`, `small_caps` (visual hint), `shadow` or `sprite` metadata. The tool does not parse MiniMessage or expand placeholders. Put literal snippets in `implementation_notes`; these display as code. All HTML content is escaped.

```json
{
  "server": "Astra",
  "mode": "Survival",
  "palette": {"accent": "#67D4AF", "text": "#F2F5EF", "muted": "#AAB7AE"},
  "sidebar": {"title": "ASTRA", "rows": [
    {"label": "Para", "value": "1.250", "kind": "stat"},
    {"label": "Bölge", "value": "Orman", "kind": "stat"},
    {"kind": "space"},
    {"text": "market.example", "kind": "footer"}
  ]},
  "tab": {"header": ["ASTRA · Survival", "34 oyuncu çevrimiçi"],
    "groups": [{"name": "Oyuncular", "players": ["[VIP] Deniz", "Ece", "Mert"]}],
    "footer": ["/yardım · market.example"]},
  "implementation_notes": ["Para placeholder'ını hedef eklentide doğrulayın."],
  "assumptions": ["Oyuncu adı ASCII varsayıldı; doğrulanmadı."],
  "compatibility": {"parser_verified": false, "glyphs_verified": false, "in_game_verified": false}
}
```

For fine styling, use `segments` instead of a string: `[{"text":"ᴏɴʟɪɴᴇ","color":"#AAB7AE"},{"text":" 34","color":"#67D4AF","bold":true}]`. A sprite segment uses `{"sprite":"minecraft:items:item/emerald","fallback":"Para"}` and appears as a labeled approximation, never the actual game texture. `kind` values: `stat`, `text`, `space`, `footer`, `separator`; prefer `space` over ornaments. `assumptions` lists every unverified fact the design depends on (placeholder support, glyph coverage, player-name script); each item renders in the preview so nothing is silently assumed. Segments with `"small_caps": true` containing İ/ı/ş/ğ/ç/ö/ü (or q) raise a report signal. `--report` emits compact JSON signals and a provisional rubric; `--strict` fails on invalid input. The HTML switches between sidebar and TAB, wide and narrow views, over illustrative game scenery.
