# 00 — Reference Index

Full routing table for Phase 3. Load only the rows matching detected needs.

| Need | Load |
|---|---|
| command semantic vocabulary | `01-command-taxonomy.md` |
| token/tree structure | `02-command-grammar.md` |
| argument types/order | `03-argument-design.md` |
| flags/options | `04-flags-and-options.md` |
| resource lifecycle | `05-resource-lifecycle.md` |
| property mutation/edit namespace | `06-property-editing.md` |
| ordered collections/actions/triggers | `07-collections-and-actions.md` |
| help/errors/discovery | `08-discovery-help-errors.md` |
| permissions/security | `09-permissions-security.md` |
| player/admin/console context | `10-player-admin-console.md` |
| completion | `11-tab-completion.md` |
| compatibility/migration | `12-compatibility-migrations.md` |
| scenario selection | `13-scenario-routing.md` |
| Skript | `14-skript.md` |
| final audit | `15-command-audit.md` |
| anti-patterns | `16-anti-patterns.md` |
| architecture decision process | `17-decision-engine.md` |
| nesting/argument complexity | `18-command-complexity.md` |
| canonical vocabulary decisions | `19-command-vocabulary.md` |
| command namespace collisions | `20-command-collision.md` |
| user workflow simulation | `21-command-journey-testing.md` |
| code semantics → user semantics | `22-semantic-mapping.md` |
| destructive operations | `23-risk-destructive-operations.md` |
| executor context | `24-context-model.md` |
| docs/help synchronization | `25-documentation-sync.md` |
| capability-oriented permissions | `26-permission-architecture.md` |
| implementation framework | `27-framework-adapters.md` |
| command AST | `28-command-ast.md` |
| repository command search | `29-project-command-forensics.md` |
| evidence strength | `30-evidence-model.md` |
| complete UX surface refactoring | `31-command-ux-refactoring.md` |
| journey matrix | `32-command-journey-matrix.md` |
| command surface sync | `33-command-surface-sync.md` |
| risk policy | `34-command-risk-policy.md` (extends 23) |
| framework adapter details | `27-framework-adapters.md` (single source; `35-command-framework-adapters.md` is a merged pointer) |
| AST operations | `36-command-ast-operations.md` |
| benchmark methodology | `37-benchmark-methodology.md` |
| regression policy | `38-regression-policy.md` |
| self audit | `39-self-audit.md` |
| pattern capture | `40-pattern-capture.md` |
| pattern format | `41-pattern-library-format.md` |
| confidence/uncertainty | `42-confidence-and-uncertainty.md` |
| public API contract | `43-command-api-contract.md` |
| migration playbook | `44-migration-playbook.md` |
| Folia/threading/async safety | `45-folia-threading.md` |
| version/platform matrix | `46-version-matrix.md` |
| proxy/network commands | `47-proxy-network.md` |
| messages/localization (MiniMessage) | `48-messages-localization.md` |
| economy/cooldown/confirmation UX | `49-economy-cooldown.md` |
| integration contracts | `50-integration-contracts.md` |
| command testing | `51-command-testing.md` |
| manifest sync (plugin.yml) | `52-plugin-manifest-sync.md` |
| interactive help/chat UX | `53-interactive-help.md` |
| command microcopy | `54-microcopy.md` |
| completion at scale | `55-completion-at-scale.md` |

Then load matching files under `references/scenarios/` and, where useful, `references/exemplars/`.

Related-file notes:

- `09` is the security baseline; `26` is the capability-tree extension. Read 09 first, 26 only when designing granular staff permission trees.
- `23` is the risk taxonomy; `34` is the enforcement policy. Read 23 first, 34 when bulk/destructive/system operations exist.
- `27` is the single framework-adapter source (the old `35` stub was merged into it).

## Phase 5 domain model schema

```yaml
project:
  platform:
  versions: []
  framework:
  public_audience:

domain:
  primary_resources: []
  secondary_resources: []
  lifecycle_operations: []
  relationships: []
  properties: []
  collections: []
  triggers: []
  actions: []

current_command_surface:
  roots: []
  tree: []
  aliases: []
  permissions: []
  contexts: []
  completion: []

compatibility:
  documented_commands: []
  internal_calls: []
  integration_calls: []
  scripts: []
  gui_actions: []
  migration_risk: low|medium|high
```
