# Showcase — Legacy Warp Plugin Redesign (v4.1 full track, synthetic fixture)

A synthetic but realistic legacy warp plugin, redesigned end-to-end with this skill. Every input file is labeled OBSERVED; everything derived is labeled INFERRED or PROPOSED per the evidence model (30).

## Before (observed)

```text
/warp <name>        travel (charges $50, 10s cooldown, silent on failure)
/warp set <name>    create/overwrite at executor location (no confirm on overwrite!)
/warp del <name>    delete immediately (no confirm, no audit)
/warplist           plain text dump, no pages, no click
```

Pain: overwrite and delete are one typo away from data loss; cost/cooldown invisible; console unsupported; `plugin.yml` declares none of the permissions the code checks.

## After (proposed)

```text
/warp go <name>            travel, confirm names cost, clickable warp list
/warp list [--page n]      paginated, clickable, permission-filtered
/warp <name>               alias, preserved (43)
/warpadmin create <name>   explicit create; overwrite requires --force + confirm
/warpadmin move <name>     region-safe relocate (45)
/warpadmin delete <name>   destructive, named-scope confirm + audit (23/34)
/warplist                  alias to /warp list
/warp set|del              deprecated with replacement notice, removal in 2.0 (44)
```

## Files

| File | Phase | Content |
|---|---|---|
| `legacy-plugin/` | 1 | observed inputs: plugin.yml, handler sketch, config, docs |
| `forensics.md` | 1 | filled forensics report |
| `evidence-ledger.md` | 2 | OBSERVED/INFERRED/PROPOSED ledger |
| `new-ast.json` | 9 | `/warp` root, validates against schema |
| `new-ast-admin.json` | 9 | `/warpadmin` root, validates against schema |
| `help-output.md` | 12 | rendered player-facing help + errors (53/54 applied) |
| `migration.md` | 12 | old→new disposition table (43/44) |
| `audit.md` | 14 | final audit: PASS WITH NOTES |

Verify: `python tools/ast_lint.py showcase/warp-redesign/new-ast.json` and `new-ast-admin.json` → 0 errors.
