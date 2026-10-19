---
name: ensisdev-mc-command-system
description: Use when designing, reviewing, refactoring or migrating Minecraft Paper/Folia/Spigot/Bukkit plugin or Skript commands — Brigadier/Cloud/CommandAPI trees, tab-completion, permission nodes, player/admin/console command UX, interactive chat help, command microcopy, or plugin.yml/paper-plugin.yml sync.
version: 4.2.0
license: MIT
---

# ensisdev-mc-command-system v4.2

## Mission

This skill is a **Minecraft command architecture intelligence library**. It is designed to let an agent read an existing plugin/Skript project and decide how that project's commands should be organized for real users.

It does not impose one global command style. It derives a style from:

- the project's domain;
- existing public behavior;
- implementation capabilities;
- player/admin/console workflows;
- compatibility constraints;
- integrations and automation;
- the command-design references in this skill.

The agent must design commands as a stable user API, not as a thin wrapper around Java/Kotlin methods or Skript internals.

## Operating invariant

**Observe → classify → model → route references → generate candidates → compare → select → model as AST → implement → synchronize → journey-test → audit.**

Never jump directly from source code to new command names.

## Reading rule (progressive disclosure)

Do NOT read every reference by default. Read this `SKILL.md` first (it is the complete process contract), then load only the references in the Phase 3 routing table that match detected needs. Each reference file is self-contained for its decision dimension. A typical task needs 3–7 references, never all 50+.

---

# 1. Mandatory workflow

## Phase 0 — Orient (cheap)

Establish in under a minute:

- project type: Paper / Folia / Spigot / Bukkit / Skript / proxy-adjacent;
- approximate size: single command, small tree (<10 leaves), large tree;
- task type: new design, review, refactor, migration, bug fix.

Then choose the track:

- **Full track** (default for non-trivial work): Phases 1–14 below.
- **Lite track** (Section 5): single-command or small-tree tasks with low migration risk. Lite still produces an AST fragment, permission notes and journey checks, but skips candidate generation and pattern capture.

## Phase 1 — Project forensics

Inspect the whole project enough to establish:

- platform and Minecraft version range;
- language/build system;
- command framework or raw Bukkit/Paper/Skript mechanism;
- plugin purpose and domain vocabulary;
- persistent resources/entities and lifecycles;
- current command tree and aliases;
- permission nodes and permission inheritance;
- tab completion/argument parsers;
- player/console support;
- configuration and persistence;
- GUI/NPC/hologram/Skript/automation command references;
- public documentation;
- tests and build tasks;
- migration/compatibility constraints.

Search broadly for command execution, not only registration. At minimum inspect usages similar to:

```text
onCommand
CommandExecutor
TabCompleter
Brigadier
CommandAPI
Cloud
dispatcher
registerCommand
executeCommand
dispatchCommand
performCommand
console command
player command
make ... execute command
```

Also inspect `.sk`, `.skrypt`, resource-pack/data folders, GUI configuration and documentation when the project suggests those surfaces exist.

Use `references/29-project-command-forensics.md`.

## Phase 2 — Evidence model

Every important statement about the current project must be classified as:

```text
OBSERVED  = directly found in the repository/runtime-facing configuration.
INFERRED  = logically derived from observed facts.
PROPOSED  = a new design recommendation, not current project behavior.
```

Never silently convert an inference or proposal into an observed fact.

Use `references/30-evidence-model.md` and record confidence with `references/42-confidence-and-uncertainty.md`.

## Phase 3 — Reference routing

Load only the references relevant to detected needs. The full 55-row routing table (which file covers which decision dimension) lives in `references/00-reference-index.md` — read it to pick your 3–7 files, then load only those. Then load matching files under `references/scenarios/` and, where useful, `references/exemplars/`.

## Phase 4 — Scenario detection

Map the project to one or more domains using `13-scenario-routing.md`.

A plugin may compose scenarios. Example:

```text
NPC system
= entity-resources
+ spatial-systems
+ action-trigger-systems
```

Do not flatten every project into the same resource/edit pattern.

## Phase 5 — Build the domain model

Create an internal model following the domain model schema in `references/00-reference-index.md`.

## Phase 6 — Semantic mapping

Map implementation concepts to user concepts with `22-semantic-mapping.md`.

Example:

```text
Observed code: hologramManager.clearLines()
User semantic: clear the hologram's line collection
Potential command: /hologram clear-lines <hologram>
Alternative: /hologram edit <hologram> lines clear
```

The internal method name does not decide the public command.

## Phase 7 — Generate architecture candidates

Do not immediately choose the first plausible tree. Generate 2–3 candidate command architectures when the problem is non-trivial.

Typical alternatives include:

```text
A — direct property commands
B — resource + edit namespace
C — capability/action namespaces
```

Evaluate candidates using `17-decision-engine.md`, `18-command-complexity.md`, `20-command-collision.md`, `21-command-journey-testing.md`, compatibility evidence, and project conventions.

Do not use arbitrary numeric scoring. Use evidence-based labels such as:

```text
strong fit
acceptable
conflicting
rejected
```

and record the reason.

## Phase 8 — Select a command architecture

Select the smallest coherent architecture that:

1. fits the domain;
2. preserves important public behavior;
3. minimizes unnecessary nesting;
4. keeps canonical vocabulary consistent;
5. gives common workflows short paths;
6. keeps dangerous/admin operations controlled;
7. provides discoverable completion/help;
8. can be implemented cleanly in the project's command framework.

## Phase 9 — Build the Command AST

Before implementation, model the final command tree using `28-command-ast.md`.

The AST must validate against `schemas/command-ast.schema.json` (draft 2020-12). It is the semantic source of truth for:

- syntax;
- argument types;
- permissions;
- contexts;
- completion;
- help;
- risk;
- compatibility aliases;
- documentation generation.

Required node coverage: root/node/argument/flag/permission/context/completion/help/risk/aliases/deprecation/implementation. AST operations (diff, merge, alias-resolve) follow `36-command-ast-operations.md`.

Do not create separate contradictory definitions of the command tree where the project architecture allows a single source of truth.

## Phase 10 — Complexity/collision/risk/threading checks

Run:

- command complexity analysis (`18`);
- root/alias collision analysis (`20`), including Vanilla and proxy roots;
- destructive-operation analysis (`23` + `34`);
- permission architecture review (`09` + `26`);
- context review (`10` + `24`);
- Folia/threading review (`45`) when the platform is Folia or async work exists;
- version-matrix review (`46`) when multiple Minecraft versions are supported.

Fix blocking issues before implementation. Validate the AST with `tools/ast_lint.py` and `tools/collision_check.py`.

## Phase 11 — Implementation

Implement the selected architecture without leaking implementation internals into the user API.

Keep parsing/command registration, domain logic and output/presentation separated when practical.

Add or update:

- command registration (via the `27` framework adapter);
- argument parsing;
- permission checks;
- completion;
- errors/help;
- compatibility aliases;
- tests (`51`).

Apply `53-interactive-help.md` to help/list/error rendering and `54-microcopy.md` to every user-facing string during implementation, not as an afterthought.

## Phase 12 — Synchronization

Use the same final command AST to update all relevant surfaces (`25`, `33`, `52`):

- README;
- command documentation;
- examples;
- generated help data;
- `plugin.yml` / `paper-plugin.yml` entries;
- `messages.yml` / localization bundles;
- migration notes;
- tests.

Use `tools/manifest_sync.py` to diff the AST against the manifest. Run `25-documentation-sync.md`. Consult the worked example in `showcase/warp-redesign/` when shaping a resource redesign.

## Phase 13 — Journey testing

Test real user goals, not only individual command methods. Cover happy and failure paths: at minimum the three most important workflows discovered during forensics, plus permission-denied and invalid-input paths. Include console when supported.

Minimum journey list:

1. first-time discovery;
2. common player/admin workflow;
3. property mutation;
4. invalid input recovery;
5. missing permission;
6. console use where supported;
7. tab-completion navigation;
8. destructive action (with confirmation where required);
9. compatibility alias;
10. integration-triggered command execution when applicable.

Use `21-command-journey-testing.md` and the `32-command-journey-matrix.md` coverage matrix.

## Phase 14 — Benchmark, self-audit, pattern capture

1. **Benchmark/regression:** compare produced AST/decision semantics with available benchmark fixtures (`benchmarks/`, methodology `37`, regression policy `38`). Textual identity is not required; semantic equivalence is the goal. Run `tools/validate_package.py`.
2. **Self-audit:** use `39-self-audit.md` before finalizing. Unresolved issues become warnings in the final audit.
3. **Pattern capture:** only after a successful redesign may a reusable pattern be captured. Strip project names and implementation details. Store generalized patterns under `patterns/` using `41-pattern-library-format.md`.
4. **Final audit:** run `15-command-audit.md` and report:

```text
COMMAND ARCHITECTURE AUDIT
Result: PASS | PASS WITH NOTES | FAIL

Observed:
...

Inferred:
...

Proposed:
...

Blocking issues:
...

Non-blocking notes:
...

Compatibility:
...

Journey tests:
...
```

---

# 2. Core design laws

1. **Domain first.** Project vocabulary is authoritative.
2. **Commands are user APIs.** Method/class names are not commands.
3. **One meaning, one canonical verb.** Compatibility aliases do not create divergent implementations.
4. **Lifecycle and mutation are different concepts.** Group them only when grouping improves discoverability.
5. **Collections need sequence semantics.** Add, insert, set, remove, clear and reorder are different operations.
6. **Spatial directions must be explicit.** `/teleport` must not leave target direction ambiguous.
7. **Flags are modifiers.** Do not use flags to hide core command identity.
8. **Discoverability is correctness.** Help and completion are part of the feature.
9. **Permissions express capabilities.** Avoid permission trees that simply mirror Java packages.
10. **Compatibility is deliberate.** Preserve public behavior when evidence shows it matters.
11. **Risk scales with operation.** Destructive and privileged actions require stronger controls.
12. **Context matters.** Player, console, automation, GUI and NPC invocation can have different input constraints.
13. **Evidence matters.** Observed, inferred and proposed facts must stay distinct.
14. **Reference projects teach patterns, not names.** FancyHolograms and FancyNpcs are exemplars, not command templates.
15. **Prefer simplicity over symmetry.** Do not add layers merely because other parts of the tree have them.

---

# 3. Fancy reference policy

When FancyHolograms/FancyNpcs are relevant, read their exemplar files and, where internet access is available, verify the current official documentation before making time-sensitive claims about their present command surface.

Use them to study patterns such as:

- durable resource lifecycle;
- inspection commands;
- grouped property editing;
- explicit spatial direction;
- filters/sorts as flags;
- ordered action lists;
- permission granularity;
- plugin-level administration.

Never copy their exact command tree merely because the target plugin is another Minecraft plugin.

---

# 4. Completion rule

Do not finish with “commands implemented” alone. A command redesign is complete only when the semantic model, implementation, completion, permissions, errors, compatibility and user journeys agree.

---

# 5. Lite track (small tasks)

Use the lite track when ALL of these hold:

- the task touches one command or a tree with fewer than ~10 leaves;
- migration risk is low (no documented public API, no external integrations calling the commands);
- no destructive/bulk/system operations are involved.

Lite workflow: Phase 1 (scoped forensics) → Phase 2 (short evidence ledger) → Phase 5 (minimal domain model) → Phase 9 (AST fragment) → Phase 10 (collision + risk skim) → Phase 11 → Phase 12 (manifest + help only) → Phase 13 (happy path + one failure path) → Phase 14 audit (short form).

Lite outputs: AST fragment validating against the schema, permission/context notes, manifest diff, 2+ journey results. Skip candidate generation (Phase 7), benchmark comparison and pattern capture.

If lite forensics discovers hidden integrations, public documentation or destructive operations, escalate to the full track.

---

# 6. Validation, UX refactoring and pattern evolution

For v4.1, the skill is not complete when code compiles. A command redesign is complete only after the command surface, UX surfaces, compatibility surfaces and documentation agree.

Use this lifecycle:

```text
FORENSICS -> EVIDENCE -> SCENARIOS -> SEMANTIC MAPPING
-> CANDIDATES -> DECISION -> COMMAND AST -> IMPLEMENTATION
-> UX SURFACE SYNC -> JOURNEY TESTS -> BENCHMARK/REGRESSION
-> SELF-AUDIT -> PATTERN CAPTURE
```

Full-track UX refactoring follows `31-command-ux-refactoring.md`: when a command changes, inspect registration, handlers, permissions, completion, help, errors, README/docs, GUI actions, NPC/hologram actions, Skript, configuration examples, automation/console calls and tests. Do not claim migration is complete while a known public surface still points at the old contract unless it is intentionally preserved.

# 7. Non-negotiable v4 invariants

1. Existing behavior is evidence, not automatically the ideal architecture.
2. FancyHolograms and FancyNpcs are exemplars, never templates.
3. Internal code names never automatically become public command names.
4. A command change is a UX migration, not merely a parser change.
5. The AST is the architectural source of truth.
6. Common workflows should become easier, not merely different.
7. Compatibility must be deliberate: preserve, alias, deprecate or migrate; never silently break.
8. Every structural change needs a reason traceable to project evidence or a reference rule.
9. Do not add references merely for coverage; each reference must represent a distinct decision dimension.
10. Pattern capture generalizes principles rather than copying examples.
