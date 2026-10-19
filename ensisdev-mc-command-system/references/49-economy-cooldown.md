# 49 — Economy, Cooldown and Confirmation UX

## Purpose

Designs commands that cost something (money, items, cooldown time) or need explicit user confirmation. Cost and confirmation are user-visible semantics: they belong in syntax, help and errors, not hidden in handler code.

## Cost as contract

- If a command charges Vault money or consumes items, the price is part of the leaf contract: `/warp go <name> ($50)` shows cost in help and in the confirm prompt.
- Insufficient-funds is a domain error (08), never a usage error: state the cost and the balance, and do not consume anything.
- Admin/bypass permissions (`plugin.economy.bypass`) must be explicit capabilities (09/26), never silent op-checks.
- Prices that vary (per-world, per-warp) complete and display per-target: `/warp go desert  ($200)` vs `/warp go spawn (free)`.

## Cooldowns

- Cooldown duration is documented in help when user-visible: `/kit claim <kit> (cooldown 24h)`.
- Remaining time is a domain error with the exact wait: `Available in 3h 12m`, not `Too soon`.
- Cooldown bypass is a separate capability from command access.
- Cooldown storage must survive restarts for meaningful durations; in-memory-only cooldowns are a documented limitation, not a silent reset.

## Confirmation flow

Two-step confirm is the default for destructive and all charged operations:

```text
/shop buy diamond  ($500)
> Confirm: buy diamond for $500? Type /shop confirm within 30s.
/shop confirm
> Purchased diamond for $500.
```

Rules:

- The prompt names action + target + cost/scope (34). A bare `Are you sure?` is a defect.
- One pending confirmation per player; a new command replaces the old pending state explicitly.
- `confirm` is a reserved leaf on roots that use the flow; do not also use `confirm` as a resource verb on the same root.
- Console/automation callers bypass interactive confirm with an explicit `--confirm` flag or dedicated non-interactive path — never by faking a player session.

## Refund and reversibility

Where the domain supports it (shop buy-back, claim unclaim window), offer the reverse path adjacent to the forward path (`/shop sell` next to `/shop buy`) and document the window. Irreversible operations say so in the confirm prompt.
