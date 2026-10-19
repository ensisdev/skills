# Migration record — LegacyWarps 1.x → 2.0 (43/44)

| Old path | Disposition | New path | Removal | Surfaces updated |
|---|---|---|---|---|
| `warp <name>` | alias | `warp go <name>` | — | docs (players.md) |
| `warplist` | alias | `warp list` | — | docs |
| `warp set <name>` | deprecate | `warpadmin create <name>` | 2.0 | docs |
| `warp del <name>` | deprecate | `warpadmin delete <name>` | 2.0 | docs |

```yaml
contract:
  version: 2.0.0
  roots: [warp, warpadmin]
  breaking_changes_since_last: []
  deprecated_paths: ["warp set <name>", "warp del <name>"]
  removal_schedule:
    - path: warp set <name>
      remove_in: "2.0"
    - path: warp del <name>
      remove_in: "2.0"
```

No internal integration callers existed (E-009), so no code migration was needed. Deprecation warnings name the replacement (44 message shape).
