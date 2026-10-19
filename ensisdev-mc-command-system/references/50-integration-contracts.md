# 50 — Integration Contracts

## Purpose

Defines how non-command surfaces invoke commands, so Phase 12 sync has a closed list instead of an open-ended hunt.

## Integration inventory

Every project gets this checklist in Phase 1 forensics; check each, mark absent explicitly:

```text
GUI menus (click actions -> command strings or direct calls)
NPC interactions (click/trigger -> commands)
hologram actions (click lines -> commands)
scheduled tasks / automation (console dispatch on timer/event)
command blocks / RCON / external dashboards
Skript files calling plugin commands
PlaceholderAPI expansions reading command-managed state
Vault / economy hooks charging for commands
LuckPerms contexts gating command access
docs / wiki / examples embedding command strings
tests invoking commands
```

## Contract rules

1. **Command strings are API calls.** A GUI action running `hologram edit ...` depends on the 43 contract exactly like a player typing it. Changing the path without updating the caller is breaking.
2. **Prefer direct calls internally.** New code should call the domain operation, not dispatch its own command string through console — dispatch is reserved for genuinely external surfaces (command blocks, Skript, cross-plugin).
3. **Context downgrade is explicit.** When a player-clicked GUI runs a console command, the AST node records both contexts and the permission actually checked (24).
4. **Placeholder/state reads** are `read`-risk (23) but still contract: renaming a resource breaks `%plugin_name%` outputs the same way renaming a command breaks scripts.
5. **RCON/command-block callers** get the `automation`/`rcon` contexts with least privilege; privileged-execution leaves (23) require review before any integration may call them.

## Sync record

```yaml
integrations:
  - surface: gui/menus.yml
    invokes: ["warp go <name>", "shop buy <item>"]
    mechanism: command-string
    migrated_to: []
  - surface: scripts/rewards.sk
    invokes: ["crate give <player>"]
    mechanism: console-dispatch
    migrated_to: []
```

All entries must be `migrated_to` the new path or dispositioned per 44 before Phase 14 passes.
