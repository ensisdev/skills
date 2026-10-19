---
name: ensisdev-mc-blockdisplays
description: "Use when planning or scaffolding a Minecraft block-display scene (interior or set-piece builds made of display entities rather than placed blocks) — e.g. a tavern, kitchen, castle hall, server room, spaceport, or any of the 30 scene categories catalogued here. Also use when asked what scenes are available, or for the budget/anchor rules for a given scale."
license: MIT
---

# Minecraft Block-Display Scene Planner

## What this skill is

A catalog of **scene planning entries** for Minecraft block-display builds
(builds made of `item_display` / `block_display` / `text_display` entities,
not placed world blocks). Each entry in `scenes/` is a YAML planning document
for one category at one scale — it fixes the conventions a build of that kind
should follow, not the build itself.

**This skill does not contain finished builds.** There are no block ids,
no coordinate offsets, no rotation/scale transforms, and no NBT in any
`scenes/*.yaml` file. Treat every entry as a spec sheet you fill in when you
actually construct the scene (by hand, by command, or via a generation
script), not as a lookup table of blocks to place.

## When to use this

- The user asks to build, plan, or scaffold an interior or set-piece scene
  in block-display form (a tavern, kitchen, castle hall, server room,
  spaceport, etc.)
- The user references one of the 30 categories below, in any scale
- The user asks what scenes are available, or for the budget/anchor rules
  for a given scale

## How to use the catalog

1. **Look up the entry first.** Check `scenes/INDEX.md` for the exact
   filename (`scenes/<category>-<scale>.yaml`) before improvising planning
   rules. The asset search policy inside each entry (`exact -> alias/tag ->
   component -> primitive -> compose`) describes the order to resolve any
   *build* asset once you're constructing — apply that same order to
   resolving *scene entries*: exact filename match first, then category/tag,
   then fall back to the nearest scale of the same category, then compose
   from primitives described below.
2. **Read the entry's fields** and apply them to the actual build:
   - `layout_spaces` — the coordinate spaces available when placing
     displays (WORLD, ANCHOR, OBJECT_LOCAL, PARENT_LOCAL, PART_LOCAL).
     Pick the narrowest space that keeps the piece easy to move as a unit.
   - `anchor_policy: explicit` — every scene needs a defined anchor point;
     never spawn displays relative to an implicit or unset origin.
   - `performance_budget` — the maximum entity count for that scale. Stay
     under it; if the intended build needs more, either move to the next
     scale up or apply the `lod_policy` (use LOD tiers for repeated or
     distant elements instead of full-detail copies).
   - `lifecycle` — the scene, not the individual display entities, owns
     spawn and teardown. Never leave orphaned display entities if the
     owning scene is removed.
   - `validation` — the three checks (anchor-defined, cleanup-defined,
     entity-budget-defined) every constructed scene must satisfy before
     it's considered complete.
3. **Only then produce the actual build data** (block/item ids, per-display
   transforms, NBT) for the user's request, following the picked entry's
   budget and anchor/lifecycle rules. This skill doesn't hand you that data —
   generate it to fit the space, theme, and budget the entry specifies.

## Categories and scales

30 categories × 4 scales (`small`, `medium`, `large`, `hero`) = 120 entries.

Categories: bedroom, blacksmith, castle-hall, cathedral, control-room,
crypt, cyberpunk-alley, dungeon, greenhouse, harbor, kitchen, laboratory,
library, living-room, magic-workshop, market, medieval-bedroom,
modern-office, museum, observatory, office, restaurant, server-room, shop,
spaceport, tavern, temple, throne-room, train-station, workshop.

Entity budgets by scale (fixed across every category):

| scale  | performance_budget |
|--------|---------------------|
| small  | 64                  |
| medium | 128                 |
| large  | 256                 |
| hero   | 384                 |

## Common mistakes

- Reading `scenes/*.yaml` as literal build data (block ids, coordinates, NBT) instead of planning conventions — it never contains any.
- Spawning displays with an implicit or unset origin instead of the required explicit anchor.
- Skipping `lod_policy` for repeated/distant elements and blowing past the scale's `performance_budget` instead of moving to the next scale.
- Leaving orphaned display entities behind when the owning scene is removed — the scene, not individual entities, owns lifecycle.

## Extending the catalog

If a request needs a category or scale not listed, compose a new entry by
copying the nearest existing one and adjusting `id`, `name`, `base_scene`,
`scale`, and `performance_budget` to match the table above — keep
`layout_spaces`, `anchor_policy`, `asset_search_policy`, `lifecycle`,
`lod_policy`, and `validation` identical, since those are fixed conventions,
not per-scene choices.
