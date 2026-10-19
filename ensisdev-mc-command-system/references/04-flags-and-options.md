# 04 — Flags and Options

## Purpose

Defines when named flags should be used and how they should behave.

## Use flags for modifiers

Flags are best for optional changes that:

- do not define the primary identity of the operation;
- can appear in varying combinations;
- would make positional argument ordering confusing;
- express creation context or filters.

Examples:

```text
/create <name> [--world <world>] [--type <type>]
/list [--type <type>] [--sort <sort>]
/nearby [--radius <radius>] [--type <type>]
```

## Do not flag the obvious

Do not turn the core resource identity into a flag:

```text
/root create --name <name>
```

when:

```text
/root create <name>
```

is clearer.

## Boolean flags

Use a boolean flag when the presence of the flag is meaningful and unambiguous. Otherwise accept an explicit state.

## Filter flags

Filtering belongs naturally on enumeration commands:

```text
/list [--type] [--world] [--sort]
/nearby [--radius] [--type] [--sort]
```

Do not add arbitrary filter flags to mutations unless they support a meaningful bulk operation.

## Bulk operations

Bulk changes must be visibly intentional. Prefer:

```text
/root remove <selector> --confirm
```

over an implicit "many" operation hidden inside a normal single-target command.

## Flag naming

Use stable long names. Keep short aliases only for frequent flags and only when the framework supports them cleanly.

Good:

```text
--radius
--world
--type
--sort
--force
--confirm
```

Avoid cryptic custom flags.

## Flag precedence

If both positional and flag forms exist for the same concept, define a single precedence rule and document it. Prefer one canonical representation whenever possible.
