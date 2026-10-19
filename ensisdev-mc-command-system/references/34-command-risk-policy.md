# 34 — Command Risk Policy

## Purpose

Enforcement policy on top of the `23-risk-destructive-operations.md` taxonomy. Where 23 classifies risk, this file decides what the architecture must require.

## Policy table

```text
read              -> no permission required by default; never gate behind admin nodes
mutate            -> capability permission + explicit target; console allowed only with explicit location/scope args
destructive       -> capability permission + explicit target + confirmation when recovery is not automatic
bulk-destructive  -> admin permission + explicit scope selector + confirmation or dry-run preview; never implicit wildcard
system            -> admin/console permission; prefer console-only; audit-log every execution
```

## Confirmation rules

- Confirmation must name the scope: `/region remove shop-* --confirm` states how many regions match before confirming.
- Prefer two-step confirm (`command` → `command confirm`) over a bare `--confirm` flag when the project framework supports stateful confirm; flags are acceptable when it does not.
- Confirmations expire. Default window: 30 seconds unless the project documents otherwise.
- A confirmed destructive command logs actor, timestamp, scope and result.

## Preview rules

Bulk operations should offer a preview where the project supports it:

```text
/region remove shop-* --dry-run
matched: 14 regions (list first 10 in completion/help output)
```

If the framework cannot preview, the help text must state the scope rule explicitly.

## Forbidden shapes

```text
/root remove all              (implicit total scope, no confirmation)
/root confirm                  (confirmation without naming scope)
/op-like run <arbitrary>       (privileged execution without review, see 23)
silent bulk from GUI click     (no actor confirmation on destructive GUI actions)
```

## Audit hook

Every `destructive`, `bulk-destructive` and `system` AST node must carry `risk` plus an `implementation.audit` note (log target). Missing audit metadata is a Phase 10 blocking issue.
