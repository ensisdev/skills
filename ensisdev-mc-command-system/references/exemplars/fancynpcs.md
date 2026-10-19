# Exemplar — FancyNpcs

## Role in this skill

FancyNpcs is a reference implementation for resource management, direct property operations, spatial semantics, filters, capability permissions and ordered action/trigger systems.

## Verified reference surface

Official documentation currently describes `/npc` as the main command for creating, modifying and removing NPCs. It documents lifecycle commands such as `help`, `create`, `copy`, `remove`, `list`, and `info`, plus direct customization commands such as `type`, `displayname`, `skin`, `equipment`, `glowing`, and `scale`. It separately documents location/rotation commands, filtering/sorting options, and interaction actions. citeturn659017search3

The same command documentation describes an action namespace with add/remove/reorder/clear/list operations tied to an NPC and trigger. citeturn659017search3

The official action-system documentation describes action types including message, console command, player command and an elevated player-command mode, and explicitly warns that elevated execution can be a security risk. citeturn659017search2

The plugin-level `/fancynpcs` command is used for system administration such as version, feature flags, reload and save. citeturn659017search4

## Patterns to extract

### 1. Lifecycle + inspection form a stable resource shell

```text
create
copy
remove
list
info
```

### 2. Some properties deserve direct commands

The project uses direct commands for high-value properties such as `skin`, `displayname`, `scale`, and movement. This demonstrates that `edit` is not mandatory for every resource property. citeturn659017search3

### 3. Filters are naturally expressed as options

Listing/nearby commands support filtering and sorting with flags/options. This is a useful filter pattern for resource enumeration. citeturn659017search3

### 4. Spatial direction must be explicit

The docs distinguish `move_here` (move the NPC to the player) from `teleport` (move the player to the NPC). citeturn659017search3

### 5. Ordered action sequences deserve sequence vocabulary

`add`, `remove`, `move_up`, `move_down`, `clear`, and `list` operate on an ordered list associated with a trigger. This is a strong model for action/trigger systems. citeturn659017search3turn659017search2

### 6. Privileged command execution deserves explicit security review

The official action docs warn that an elevated player-command action can be a security risk. This is evidence for the risk model in reference 23. citeturn659017search2

## What NOT to copy

Do not infer that all plugins should have:

```text
/root type
/root skin
/root displayname
/root action
```

The correct surface depends on property frequency, domain vocabulary, compatibility and command complexity.

## Source

Official FancyNpcs documentation:

- https://fancyinnovations.com/docs/minecraft-plugins/fancynpcs/commands/npc
- https://fancyinnovations.com/docs/minecraft-plugins/fancynpcs/commands/fancynpcs
- https://fancyinnovations.com/docs/minecraft-plugins/fancynpcs/tutorials/action-system

Verified: 2026-09-17.
