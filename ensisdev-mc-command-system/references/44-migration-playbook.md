# 44 — Migration Playbook

## Purpose

Step-by-step procedure for moving a live command surface from an old contract to a new one without silently breaking players, staff, scripts or integrations.

## Ladder

```text
preserve   keep the old path as canonical (cheapest; use when old path is fine)
alias      old path forwards to identical semantics (use when rename unifies vocabulary)
deprecate  old path warns + forwards, with scheduled removal (gradual migration)
migrate    update every internal caller, doc, example and test to the new path
remove     delete only when evidence + project policy permit (see 43)
```

Default preference: preserve < alias < deprecate < migrate < remove. Climb only with reason.

## Procedure

1. **Inventory** (Phase 1/29): list every surface referencing the old path — code, Skript, GUI actions, NPC/hologram actions, scheduler, docs, examples, tests.
2. **Classify** (43): assign each path a disposition and record it in the AST.
3. **Bridge**: implement alias/deprecation forwarding first, before any new-path logic change.
4. **Message**: deprecation warnings state the new path and removal version; never warn without a replacement.
5. **Migrate callers**: update internal integrations, docs, examples, `plugin.yml` usages, locale files.
6. **Verify** (33/52): manifest sync + doc sync + journey test on the old path (must still work or warn-then-work).
7. **Schedule**: record removal version; re-check at release audit (`templates/v4-release-audit.md`).

## Deprecation message shape

```text
/shop create is deprecated, use /shop add <name> instead (removal in 3.0).
```

Machine-readable marker where the project supports it (locale key, e.g. `command.deprecated`).

## Rollback rule

If a migration breaks an integration found late, restore the old path as `alias` first and re-plan; never leave a known caller pointing at a removed path while debating the ideal tree.

## Record

```yaml
migration:
  old_path: warp set <name>
  new_path: warp create <name>
  disposition: deprecate
  affected_surfaces: [docs/warps.md, gui/menus.yml, scripts/warps.sk]
  migrated: [docs/warps.md]
  pending: [gui/menus.yml, scripts/warps.sk]
  removal_version: 2.0
```
