# EnsisDev Command Architecture Benchmarks v4.1

Benchmarks test semantic decisions rather than exact text. Each case has a problem statement, scenario tags, observed input fixtures, journey requirements and pass criteria. Each golden has `requirements`, `expected_paths`, `forbidden` anti-patterns and `journey_checks`.

Cases: hologram-resource, npc-actions, player-warps, shop-items, region-admin, skript-command, gui-dispatch, legacy-migration, folia-teleport, confirm-destructive, proxy-dispatch, i18n-help.

A semantically equivalent command tree may pass even if its textual shape differs from the golden example. A single `forbidden` hit fails the case regardless of other dimensions.

Score with `SCORING.md` (weighted dimensions, PASS / PASS WITH NOTES / FAIL). Validate the package with `python tools/validate_package.py`.
