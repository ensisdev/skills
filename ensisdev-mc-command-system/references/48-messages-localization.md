# 48 — Messages and Localization

## Purpose

Synchronizes command output with the architecture: help, errors, confirmations and deprecation notices are part of the command contract (43), and MiniMessage/Adventure realities constrain what output can promise.

## MiniMessage rules

- All user-facing text goes through locale keys, never hardcoded strings in handlers. Key shape: `<root>.<leaf>.<kind>`, e.g. `hologram.create.success`.
- Escape user input injected into MiniMessage templates. A hologram name containing `<red>` must not recolor output; treat every interpolated value as untrusted.
- Document which arguments accept MiniMessage (`text`, `lore`) vs plain text (`name`, `id`). Mixed semantics on one argument is a design bug.
- Legacy `&` color codes: decide per project — support as deprecated input (translating to MiniMessage) or reject with a helpful error. Never half-translate.

## Locale bundle contract

```yaml
locales: [en, tr]
fallback: en
keys_per_leaf: [usage, success, error_usage, error_domain, error_permission, confirm_prompt]
```

Every AST leaf with user output needs its keys present in the fallback locale; other locales may fall back explicitly. Missing fallback keys are a Phase 12 blocking issue.

## Help output shape

```text
/<root> <path> <required> [optional] --flag <value>
short description (one line, verb-first)
permission note only when relevant to the reader
```

Help text is generated from the AST where the project allows it (28/33). Hand-written help must be diffed against the AST in Phase 12.

## Error taxonomy in text

Map 08 error kinds to locale keys one-to-one: usage errors point at the argument (`error_usage` + highlighted token), domain failures state state (`error_domain`), permission failures never reveal hidden structure (`error_permission` is generic).

## Multi-language vocabulary

Canonical command verbs stay English (19). Localized verbs as aliases are allowed only when the project already documents them; do not invent Turkish/Spanish alias trees speculatively — each alias is permanent contract (43).
