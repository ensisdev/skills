# EnsisDev-Mc-Command-System v4.2.0

Minecraft command architecture intelligence for existing Paper/Folia/Spigot/Bukkit plugins, command frameworks and Skript projects.

## v4.2

Adds the admiration layer: interactive chat help (53), command microcopy (54), completion at scale (55), a full worked showcase (`showcase/warp-redesign/`), and lint-clean reference ASTs for benchmark cases 01 and 03.

Command architecture + full UX refactoring + benchmark/regression + reusable pattern capture. Adds lite track for small tasks, Folia/version/proxy/i18n/economy/integration/testing/manifest references, executable tooling, full benchmark fixtures with scoring, and an expanded pattern library.

Pipeline: `forensics -> evidence -> scenarios -> semantic mapping -> candidates -> decision -> AST -> implementation -> UX sync -> journeys -> benchmark -> self-audit -> pattern capture`

FancyHolograms and FancyNpcs are exemplars only; extract principles, never copy their trees blindly.

Validate with `python tools/validate_package.py`.

Directories: `references/`, `references/scenarios/`, `references/exemplars/`, `patterns/`, `benchmarks/`, `schemas/`, `templates/`, `tools/`, `showcase/`.

## Install (opencode)

Copy or symlink this folder into your skills directory (e.g. `~/.agents/skills/` or your project's `.agents/skills/`). The skill activates on Minecraft command tasks via its `SKILL.md` frontmatter — no further setup needed.

## Usage examples

```text
Bu pluginin komut ağacını çıkar ve audit et.
Warp sistemini command AST'ye dök, eski /warp <name> yolunu alias olarak koru.
Shop komutlarını player/admin olarak ayır, purchase flow'a confirm ekle.
plugin.yml ile implementasyon drift etmiş mi kontrol et.
Folia uyumluluğu için teleport komutlarını review et.
```

Small single-command tasks automatically use the lite track (SKILL.md Section 5); large refactors use the full 14-phase track.

## Tools

| Script | Phase | Purpose |
|---|---|---|
| `tools/validate_package.py` | 14 | package integrity: files, schema shape, routing coverage, benchmarks, patterns |
| `tools/ast_lint.py` | 10 | AST depth, alias, permission/risk/help/completion coverage |
| `tools/collision_check.py` | 10 | roots/aliases vs Vanilla/proxy/ecosystem reserved roots |
| `tools/manifest_sync.py` | 12 | AST vs plugin.yml drift |
| `tools/migration_diff.py` | 14 | old vs new AST path changes with disposition skeleton |
