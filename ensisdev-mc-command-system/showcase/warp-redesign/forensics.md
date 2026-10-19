# Forensics — LegacyWarps v1.4.2 (Phase 1)

## Project

Bukkit-style warp plugin, Paper 1.20, single `CommandExecutor`, YAML store. Audience: players travel, admins curate.

## Platform / Framework

Paper 1.20 (OBSERVED: `api-version: "1.20"`), raw `CommandExecutor`, no Brigadier/Cloud/CommandAPI (OBSERVED: handler sketch). Folia-unsafe teleport (INFERRED: direct `player.teleport` in handler).

## Command roots observed

`/warp` (travel/set/del multiplexed), `/warplist`. No aliases declared (OBSERVED: plugin.yml).

## Registration locations

`WarpCommands.onCommand` — single branch chain (OBSERVED).

## Invocation locations

None internal; scheduler/automation absent (OBSERVED: no matches). Docs (`players.md`) invoke all four paths — documentation is a compatibility surface.

## Permission surface

Declared: none. Checked: none in code (OBSERVED). Any player can `/warp del` — critical finding.

## Completion surface

None (OBSERVED). No TabCompleter.

## Documentation references

`players.md` documents set/go/del/warplist (OBSERVED) — all four are contract (43).

## Integration callers

Docs only. No GUI/Skript/scheduler callers found (OBSERVED ABSENT).

## Compatibility hotspots

1. `/warp <name>` player muscle memory + docs → must survive (alias).
2. `/warp set|del` documented → deprecate, not remove (44).
3. Silent overwrite on `set` → data-loss risk, needs `--force` + confirm.
4. Console crashes (`(Player) sender` cast) → explicit contexts (10/24).
