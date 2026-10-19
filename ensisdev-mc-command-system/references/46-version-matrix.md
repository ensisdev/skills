# 46 — Version and Platform Matrix

## Purpose

Designs one command surface that survives the project's supported version range (Spigot / Paper / Folia × Minecraft versions) without forking user-visible semantics per version.

## Matrix

Record during Phase 1 forensics:

```yaml
platform_matrix:
  platforms: [paper]          # paper | folia | spigot | bukkit
  mc_versions: ["1.20.4", "1.21"]
  mappings: mojang            # mojang | spigot
  command_backend: brigadier  # bukkit | brigadier | commandapi | cloud
```

## Known fracture points

```text
1.20.5+ Brigadier changes     -> argument/behavior drift; verify literal/redirect handling per version
Mojang-mapped vs Spigot-mapped -> NMS-adjacent registration paths differ; keep behind adapter (27)
paper-plugin.yml vs plugin.yml -> Paper-only loader fields; see 52
Folia-only schedulers         -> see 45; never expose scheduler choice in command syntax
legacy chat color codes       -> MiniMessage migration; see 48
```

Do not invent a fracture point. Verify against the project's build files (`build.gradle`, version ranges, CI matrix) — OBSERVED, not assumed.

## Design rules

1. **One public tree.** Version differences live in the adapter, never in user-visible paths. No `/cmd-v2` versioned roots.
2. **Capability detection over version sniffing** in help/completion: if a feature is unavailable on the running version, hide or disable its leaf with a reason, rather than failing at parse time with a generic error.
3. **Degrade explicitly.** When an argument type is unavailable on an old version (e.g. a Brigadier type), fall back to a validated string argument with identical user semantics and document the fallback.
4. **Test the edges.** Journey tests (21/32) must run on the oldest and newest supported versions, not only the dev version.

## Deprecation across versions

When a version floor rises (e.g. dropping 1.19), treat removed workarounds as internal cleanup, not contract changes — unless a user-visible path changes, in which case 43/44 apply.
