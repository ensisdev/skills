# 37 — Benchmark Methodology

## Purpose

Measures semantic quality, not textual similarity. A semantically equivalent tree passes even when token choices differ from the golden example.

## Fixture shape

Each case under `benchmarks/cases/` contains:

```text
Problem            the redesign task in one paragraph
Scenarios          scenario tags routing the task (13)
Input fixtures     OBSERVED snippets: manifest fragment, handler sketch, doc excerpt
Journeys           the user goals that must work end-to-end (21/32)
Pass criteria      what the produced AST must and must not contain
```

Each golden under `benchmarks/golden/` contains:

```json
{
  "requirements": ["scenario and semantic tags the AST must satisfy"],
  "expected_paths": ["canonical leaf paths that must exist (aliases allowed)"],
  "forbidden": ["anti-patterns that fail the case even if everything else passes"],
  "journey_checks": ["journey outcomes the tree must enable"]
}
```

## Scoring

Score with `benchmarks/SCORING.md`. Dimensions: lifecycle semantics, vocabulary, nesting depth, permissions, contexts, completion, risk controls, compatibility, journey outcomes. Each dimension is `pass / partial / fail` with evidence; a single `forbidden` hit fails the case.

## Regression use

Accepted benchmark runs are snapshots per `38-regression-policy.md`. Re-run after skill changes; any new `fail` on a previously passing case is a skill regression, not a model quirk, until proven otherwise.
