# 02 — Command Grammar

## Purpose

Defines how a command tree is shaped and how tokens are ordered. It does not decide what a verb means or how permissions are assigned.

## Grammar model

Think in layers:

```text
root → operation → target/resource → property/context → value/options
```

Examples:

```text
/npc create <name> [options]
/npc info <npc>
/npc edit <npc> <property> <value>
/npc action <npc> <trigger> add <action-type> [value]
```

## Root command

The root should be:

- stable;
- easy to type;
- aligned with the plugin's primary domain;
- available as the top-level help entry point.

Do not force a generic `/admin` wrapper when the project already has a meaningful domain root.

## Subcommand ordering

Within a resource-oriented root, prefer this conceptual order in help/documentation:

1. help/discovery;
2. list/search/nearby;
3. info/status;
4. create/copy;
5. edit/set/action/move;
6. remove/clear;
7. administrative commands.

Runtime registration order may differ; user-facing help should follow the conceptual order.

## Nesting depth

Use nesting only when it reduces ambiguity or groups a real conceptual namespace.

Preferred:

```text
/root edit <resource> <property>
/root action <resource> <trigger> <operation>
```

Avoid deep chains such as:

```text
/root manage resource actions trigger action set value
```

Unless every segment represents a stable public concept users actually need to select.

## Direct command vs namespace

Use a direct command when:

- the operation is a dominant workflow;
- the property is likely to be remembered;
- grouping would make the path harder to discover.

Use an `edit`/`action` namespace when:

- many sibling properties exist;
- several operations act on the same resource;
- grouping reduces root-level clutter;
- the resource is clearly identified before mutation.

## Context-sensitive verbs

A verb such as `remove` may legitimately occur in two contexts:

```text
/root remove <resource>
/root action <resource> <trigger> remove <index>
```

The namespace provides the semantic boundary. Do not invent separate global verbs merely to avoid contextual reuse.

## Canonical grammar notation

Use:

- `<name>` required value;
- `[value]` optional value;
- `[--flag <value>]` optional named modifier;
- `(a | b | c)` enumerated choices;
- `[text...]` greedy trailing input.

In implementation, preserve types rather than treating every token as arbitrary text.
