# 54 — Command Microcopy

## Purpose

The craft of the words themselves. Architecture decides what the player can do; microcopy decides whether it feels effortless. Every string below maps to an AST leaf output kind (48).

## Voice rules

```text
verb-first        Start help lines with the action: "Travel to a warp." not "This command allows travel..."
second person     Address the player: "You don't have enough money." not "Insufficient funds."
solution-bearing  Every error names the fix: "Available in 3h 12m." not "Too soon."
no jargon         "Unknown warp 'desert'." not "Resource resolution failure (id=desert)."
no blame          "That warp doesn't exist yet." not "You typed it wrong."
```

## Per-kind shapes (EN + TR)

```text
usage:    Usage: /warp go <name>            | Kullanım: /warp go <isim>
success:  Teleported to spawn.              | spawn noktasına ışınlandın.
domain:   Unknown warp 'desert'. See /warp list. | 'desert' diye bir warp yok. Bak: /warp list.
deny:     You don't have permission to do that.  | Bunu yapmak için yetkin yok.
cooldown: Available in 3h 12m.              | 3 sa 12 dk sonra kullanılabilir.
cost:     That costs $50 but you have $12.  | Ücret $50 ama bakiyen $12.
confirm:  Buy diamond for $500? Type /shop confirm within 30s. | Diamond $500 karşılığı alınsın mı? 30 sn içinde /shop confirm yaz.
deprecated: /shop create is deprecated, use /shop add <name> (removal in 3.0). | /shop create eskidi, /shop add <isim> kullan (3.0'da kalkacak).
```

## Bad → good pairs

```text
BAD   "Error: invalid input."              GOOD "Usage: /warp go <name> — try /warp list to see names."
BAD   "You can't do that."                 GOOD "That needs the moderator capability. Ask an admin."
BAD   "Are you sure? [yes/no]"             GOOD "Delete region 'shop-12' with 44 plots? Type /region confirm within 30s."
BAD   "Purged."                            GOOD "Purged 37 records older than 30 days. Logged to audit."
BAD   "Unknown command."                   GOOD "Unknown warp 'desrt'. Did you mean 'desert'? Run /warp go desert."
```

## Review gate

Phase 12 sync includes a microcopy pass: read every new string aloud against the five voice rules. A string failing two or more rules is reworked before audit. Tone stays consistent across the whole tree — one voice, not one voice per developer.
