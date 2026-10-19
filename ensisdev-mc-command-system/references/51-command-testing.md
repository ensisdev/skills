# 51 — Command Testing

## Purpose

Makes command behavior verifiable: what to test per leaf, with which harness, and what counts as coverage for the Phase 13/14 gates.

## Harness selection

```text
MockBukkit           -> registration, permission checks, basic dispatch, tab completion
Paper test framework -> Brigadier behavior, async paths, Folia-adjacent scheduling
Skript test          -> parse + trigger behavior of .sk commands (see 14)
manual journey       -> full player-feel paths that harnesses cannot render (required regardless)
```

Record the harness per project in Phase 1; "no tests" is an OBSERVED fact that raises journey-testing weight, not an excuse to skip it.

## Per-leaf test kinds

```text
parse      valid input dispatches; invalid input yields usage error (08), never silent success
permission unauthorized sender gets error_permission; completion hides the leaf
context    console/command-block behavior matches AST contexts (10/24)
completion provider returns exactly the parser-accepted set, permission-filtered (11)
risk       destructive leaves require confirmation/scope; charged leaves charge once (23/34/49)
compat     every alias/deprecated path resolves to canonical semantics (12/43/44)
locale     fallback-locale keys exist; MiniMessage templates render without leaking tags (48)
threading  region/async leaves execute on the declared scheduler (45)
```

## Coverage gate

- Full track: every leaf has parse + permission tests; every destructive/bulk/system leaf has risk + confirm tests; every alias has a compat test.
- Lite track: happy-path + one failure-path test per touched leaf.
- Journeys (21/32) are scenario-level and do not replace per-leaf tests.

## Fixture rule

Tests dispatch through the same adapter as production (27). Testing the handler method directly while production goes through Brigadier leaves the parser untested — a coverage gap, not coverage.
