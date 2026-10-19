# 18 — Command Complexity

## Purpose

Detects command structures that are technically valid but cognitively expensive.

## Dimensions

Inspect:

- nesting depth;
- required token count;
- number of peer choices;
- required argument count;
- number of optional arguments;
- mixed semantic namespaces;
- ambiguous tokens;
- context switches;
- completion burden.

## Warning patterns

### Excessive nesting

```text
/root manage resource edit property set value
```

Each token must represent a concept the user can meaningfully predict. Remove implementation hierarchy from the public path.

### Too many required tokens

If a common operation needs many required values, search for:

- a better target context;
- a flag for optional modifiers;
- a dedicated high-frequency command;
- an operation namespace that removes repetition.

### Peer explosion

If a single command has dozens of property siblings, group semantically related low-frequency properties. Do not group everything merely to reduce count.

### Mixed grammar

Avoid trees where equivalent properties alternate between:

```text
/root set X
/root edit Y
/root update Z
/root config W
```

unless the semantics are genuinely different.

## Practical thresholds

These are warnings, not absolute laws:

```text
nesting depth 1–3: normally healthy
nesting depth 4: review
nesting depth 5+: strong reason required

3–5 required arguments: review for better grouping
6+: usually redesign unless the domain itself requires it
```

The project may justify exceptions. Document them.

## Complexity review output

```text
Complexity: LOW | MODERATE | HIGH

Observed pressure:
- ...

Cause:
- ...

Preferred simplification:
- ...
```
