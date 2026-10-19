# Changelog

## 4.2.1
- Dogfood fix (EnsPillars): all tools read files as UTF-8 — Turkish locale content no longer needs ASCII workarounds (N3 obsolete).

## 4.2.0
- New references: 53 interactive help/chat UX, 54 microcopy (EN+TR), 55 completion at scale.
- Showcase: full warp-plugin redesign (legacy fixture → forensics → evidence → 2 lint-clean ASTs → rendered help → migration → PASS WITH NOTES audit).
- Benchmark golden reference ASTs for cases 01 and 03 (ast_lint + collision clean).
- Validator checks shipped ASTs and new files; SKILL routing covers 53-55.
- SKILL v4.2: interactive help + microcopy applied during implementation (Phase 11).

## 4.1.0
- SKILL.md: merged duplicate Phase 9-14 definitions into one 14-phase track, fixed section numbering, unified routing table (01-52), progressive-disclosure reading rule, lite track for small tasks.
- New references 45-52: Folia/threading, version matrix, proxy/network, messages/localization, economy/cooldown/confirm, integration contracts, command testing, manifest sync.
- New scenarios: teleport-travel, moderation-punishment, minigame-arena; routing matrix extended.
- Merged 35 into 27 (single framework-adapter source); cross-linked 09/26 and 23/34.
- Expanded stubs: 34 risk policy, 37 benchmark methodology, 39 self-audit checklist, 43 API contract, 44 migration playbook.
- Templates: fixed command-ast.yaml to validate against the schema; added plugin-yml, messages-yml, Skript, Cloud and Brigadier starters.
- Tools: hardened validate_package.py; added ast_lint.py, collision_check.py, manifest_sync.py, migration_diff.py (stdlib only, verified).
- Benchmarks: all 8 cases rewritten as full fixtures; goldens upgraded with expected_paths/forbidden/journey_checks; 4 new cases (folia-teleport, confirm-destructive, proxy-dispatch, i18n-help); SCORING.md rubric.
- Patterns: 6 new (list-inspect, confirm-destructive, bulk-admin, selector-target, admin-root, pagination-filter); added bad-command-tree anti-exemplar.
- README: opencode install, usage examples, tools table.

## 4.0.0
- Full v3 UX refactoring and command-surface synchronization.
- Benchmark methodology, 8 semantic fixtures and regression policy.
- Command API contract and migration playbook.
- Confidence/uncertainty model.
- Reusable pattern library and extraction format.
- Command AST schema upgraded to v4.
- Package validator added.

## 3.0.0
- Added command UX refactoring, journeys, risk policy and framework adapters.

## 2.0.0
- Added decision engine, AST, forensics, evidence, complexity, collision, semantic mapping and journey intelligence.

## 1.0.0
- Initial command style library.
