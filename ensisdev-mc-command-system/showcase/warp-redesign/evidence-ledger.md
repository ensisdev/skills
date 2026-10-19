# Evidence Ledger — LegacyWarps redesign (Phase 2)

| ID | Claim | Class | Repository/Reference Evidence | Confidence |
|---|---|---|---|---|
| E-001 | Roots are /warp and /warplist, no aliases | OBSERVED | plugin.yml | high |
| E-002 | No permission is declared or checked | OBSERVED | plugin.yml + WarpCommands.java | high |
| E-003 | set silently overwrites existing warps | OBSERVED | WarpStore.save in handler | high |
| E-004 | del has no confirm and no audit | OBSERVED | WarpStore.delete in handler | high |
| E-005 | Travel costs 50 with 10s cooldown | OBSERVED | config.yml | high |
| E-006 | Failures (funds/cooldown) are silent | OBSERVED | early return, no message | high |
| E-007 | Console dispatch crashes (cast) | OBSERVED | (Player) sender | high |
| E-008 | Docs teach set/go/del/warplist | OBSERVED | players.md | high |
| E-009 | No GUI/Skript/scheduler callers | OBSERVED | absent (searched) | medium |
| E-010 | Teleport is Folia-unsafe as written | INFERRED | E-007 pattern + direct teleport (45) | medium |
| E-011 | Deletion without confirm risks grief | INFERRED | E-004 + shared admin use (23) | high |
| E-012 | /warp <name> must keep working | PROPOSED | E-008 + muscle memory (43/44) | high |
| E-013 | Admin verbs move to /warpadmin root | PROPOSED | player/admin separation (pattern.admin-root) | high |
