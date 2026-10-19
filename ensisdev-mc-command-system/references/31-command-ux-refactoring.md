# Command UX Refactoring

Treat the command system as one public UX surface: tree, parser, handler, permission, completion, help, errors, documentation, integrations and tests.

Rules:
1. Identify the primary user journey before shortening syntax.
2. Keep canonical vocabulary stable across commands, help and docs.
3. Make common workflows short without semantic ambiguity.
4. Completion should reveal valid next actions.
5. Errors should identify the bad token and recovery path.
6. Preserve aliases when migration cost is high and semantics are identical.
7. A refactor is complete only when all known surfaces agree.
