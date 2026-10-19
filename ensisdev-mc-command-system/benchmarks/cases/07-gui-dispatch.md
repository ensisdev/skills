# Case 07 — GUI Dispatch

## Problem

A menu plugin's `menus.yml` fires command strings on click: `warp go spawn`, `shop buy diamond`, `crate give %player% common`. A planned warp rename (`go` → `visit`) would silently break three menus. Model the integration contract and produce a migration-safe tree.

## Scenarios

`gui-menu`, `gameplay-player`.

## Input fixtures (OBSERVED)

```yaml
# menus.yml (observed)
main-menu:
  items:
    spawn:
      click-actions: ["warp go spawn"]
    daily:
      click-actions: ["crate give %player% common"]
```

## Journeys

1. click spawn item → travel flow executes with player context;
2. rename warp verb → menus keep working via alias or migrated strings;
3. player without warp permission clicks item → generic denial, no state leak.

## Pass criteria

Integration inventory complete per 50; rename dispositioned (alias or migrate, never silent); context downgrade (GUI click → console dispatch) explicit in AST; permission denial generic.
