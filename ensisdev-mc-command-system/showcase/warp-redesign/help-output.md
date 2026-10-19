# Rendered player-facing output (Phase 12) — 53/54 applied

## /warp list (page 1/2, player view)

```text
[aqua]Warps [gray](page 1/2) — click a warp to travel ($50 each)
  [spawn]         hover: spawn — $50 — ready        click: suggest /warp go spawn
  [desert]        hover: desert — $50 — cooldown 3m  click: suggest /warp go desert
  [arena]         hover: arena — free — ready        click: run /warp go arena
[gray][← Prev] [1/2] [Next →]   click: run /warp list --page 2
```

Console renders the same information as plain text (53 fallback), no hover.

## Error renders (54 voice rules)

```text
/warp go desrt
[yellow]Unknown warp 'desrt'. Did you mean 'desert'? [Run: /warp go desert]

/warp go desert   (cooldown active)
[yellow]Available in 3m 12s.

/warp go vip      (no funds)
[red]That costs $50 but you have $12.

/warpadmin delete spawn   (admin)
/[yellow]Delete warp 'spawn' (38 visits this week)? Type /warpadmin confirm within 30s.
/warpadmin confirm
[green]Deleted warp 'spawn'. Logged to audit.

/warp set spawn   (legacy)
/[yellow]/warp set is deprecated, use /warpadmin create <name> instead (removal in 2.0).
```

## Microcopy check (54 gate)

- verb-first: "Travel…", "Delete…", "List…" — pass
- solution-bearing: every error names the fix — pass
- no jargon: "Unknown warp" not "resolution failure" — pass
- one voice across both roots — pass
