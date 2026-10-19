# 52 — Plugin Manifest Sync

## Purpose

Keeps `plugin.yml` / `paper-plugin.yml` (and their permission blocks) consistent with the AST. The manifest is a second declaration of the command surface; drift between manifest and implementation is a compatibility and discovery bug.

## What the manifest declares

```text
commands.<name>.description   -> must match AST help summary (08/28)
commands.<name>.usage         -> must be derivable from the AST path (28)
commands.<name>.aliases       -> must equal AST aliases; no extra, no missing
commands.<name>.permission    -> must equal the root AST permission (09/26)
permissions.<node>.default    -> op / not-op must match the risk class (23): read leaves default false-safe
```

## Sync procedure (Phase 12)

1. Generate the expected manifest fragment from the AST (`tools/manifest_sync.py`).
2. Diff against the project's `plugin.yml` / `paper-plugin.yml`.
3. Every diff is either fixed or dispositioned: intentional extras get a `notes` entry with reason; nothing drifts silently.
4. Paper-only projects use `paper-plugin.yml` as canonical; keep a legacy `plugin.yml` only when the version matrix (46) requires it, and generate one from the other.

## Loader-specific notes

- `paper-plugin.yml` supports `loader` hooks and Folia markers — record platform constraints (45/46) where the loader enforces them.
- Command `permission-message` in the manifest must use the same locale key as the AST `error_permission` path (48); two different denial texts for one leaf is a defect.
- `default: op` on economy/destructive/system leaves is forbidden unless the 23/34 review explicitly allows it.

## Forensics

The manifest is OBSERVED evidence (30): declared-but-unimplemented commands and implemented-but-undeclared commands are both first-class findings, reported in Phase 1 and closed by Phase 12.
