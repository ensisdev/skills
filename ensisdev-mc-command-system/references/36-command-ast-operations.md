# Command AST Operations

Transform the AST instead of rewriting command logic ad hoc. Supported conceptual operations: add-node, remove-node, rename-node, move-node, merge-alias, add-argument, change-argument, set-permission, set-context, set-risk, deprecate, add-completion, update-help.

Invariants: unique canonical paths, non-ambiguous aliases, valid argument ordering, risk metadata on destructive nodes, implementation mapping for executable nodes and discoverability through help or completion.
