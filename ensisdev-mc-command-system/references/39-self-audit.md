# 39 — Self Audit

## Purpose

Pre-completion interrogation. Run before the final audit (15). Every unresolved answer becomes a warning in the audit report.

## Checklist

Answer each with OBSERVED / INFERRED / PROPOSED evidence (30) and a confidence label (42):

```text
1. facts        Did I invent any project fact? Is each claim labeled observed/inferred/proposed?
2. exemplar    Did I copy FancyHolograms/FancyNpcs structure instead of extracting a principle?
3. internals   Did a class/method name leak into a public command path?
4. nesting     Did I add a level the domain does not need? (check 18)
5. vocabulary  Is each verb canonical per 19, with aliases recorded not duplicated?
6. collision   Did I check roots/aliases against Vanilla, proxy and sister plugins? (check 20 + tool)
7. compat      Is every changed path dispositioned per 43/44 (preserve/alias/deprecate/migrate/remove)?
8. contexts    Is player/console/command-block/rcon support explicit per node? (check 10/24)
9. permissions Is each node capability-mapped without over-granularity? (check 09/26)
10. completion  Is completion permission-filtered and parser-consistent? (check 11)
11. help/errors Does every leaf have help + usage error + domain error paths? (check 08)
12. risk        Is every mutation risk-classed with controls per 23/34? Confirmations named with scope?
13. threading   On Folia/async paths, is region/thread safety reviewed? (check 45)
14. manifest    Do plugin.yml/paper-plugin.yml match the AST? (check 52 + tool)
15. surfaces    Were docs, locales, GUI/NPC/Skript callers synced or intentionally deferred? (check 25/33)
16. journeys    Did the required journeys run, including failure paths? (check 21/32)
17. pattern     Am I promoting a one-off project decision into a universal pattern? (check 40)
```

## Output

```text
SELF-AUDIT: n passed, m warnings
WARN <item>: <reason> -> <phase to revisit or explicit acceptance>
```

Zero blocking warnings is required for PASS. Accepted warnings must state who accepts the risk and why.
