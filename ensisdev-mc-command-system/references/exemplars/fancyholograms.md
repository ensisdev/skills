# Exemplar — FancyHolograms

## Role in this skill

FancyHolograms is a **reference implementation for extracting patterns**, not a template to copy.

## Verified reference surface

Official documentation currently describes a `/hologram` resource command surface with `help`, `list`, `nearby`, `create`, `remove`, `copy`, and `info`, followed by grouped modification commands under `/hologram edit ...` for many hologram properties. It also documents a separate `/fancyholograms` administration command for operations such as `version`, `save`, `reload` and `convert`. citeturn659017search1turn659017search0

The current official getting-started documentation also demonstrates common text-hologram workflows such as create → add line → set line → background, and points to a move operation. citeturn659017search5

## Patterns to extract

### 1. Resource lifecycle is separate from property mutation

```text
/hologram create
/hologram remove
/hologram copy
/hologram info
```

versus:

```text
/hologram edit <hologram> <property> ...
```

### 2. Spatial semantics are explicit

The official command docs distinguish moving the hologram to the executor (`moveHere`) from moving it to explicit coordinates (`moveTo`). They also distinguish teleporting the player to an NPC in FancyNpcs. This is useful evidence for explicit spatial direction. citeturn659017search1turn659017search3

### 3. Rich resources need a property namespace

The hologram has many independent properties such as position, rotation, scale, billboard, visibility, lines, background and text formatting. Grouping lower-frequency mutations keeps the root readable. citeturn659017search1

### 4. Plugin administration belongs to an administration surface

`/fancyholograms version`, `save`, `reload`, and `convert` are separated from resource manipulation. citeturn659017search0

### 5. Integrations can be expressed as resource relationships

The docs include `linkWithNpc` and `unlinkWithNpc`, demonstrating a domain relationship command rather than a generic implementation operation. citeturn659017search1

## What NOT to copy

Do not automatically copy:

```text
/hologram edit ...
moveHere
moveTo
```

into every plugin. If a target project has only two editable properties, direct commands may be clearer. If its domain vocabulary differs, use that vocabulary.

## Source

Official FancyHolograms documentation:

- https://fancyinnovations.com/docs/minecraft-plugins/fancyholograms/commands/hologram
- https://fancyinnovations.com/docs/minecraft-plugins/fancyholograms/commands/fancyholograms
- https://fancyinnovations.com/docs/minecraft-plugins/fancyholograms/getting-started

Verified: 2026-09-17.
