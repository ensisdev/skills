# 27 — Framework Adapter Layer

## Purpose

Separates command architecture from the implementation framework.

## Supported families

The skill can reason about projects using:

```text
Bukkit/Paper PluginCommand
Brigadier
Paper command APIs
CommandAPI
Cloud
other command frameworks
Skript
```

Do not assume an API exists merely because it is common in Minecraft development. Inspect the repository/build dependencies.

## Adapter responsibilities

An adapter translates the command AST into framework concerns:

- registration;
- argument parser types;
- sender/context retrieval;
- permission checks;
- completion hooks;
- syntax/help exposure;
- error handling;
- aliases.

It must not invent user-facing semantics.

## Architecture boundary

```text
Command AST
   ↓
Framework adapter
   ↓
Parser/registration
   ↓
Application/domain operation
```

Domain code should not need to know whether the command arrived through Brigadier, Cloud, Bukkit or Skript.

## Framework-specific review

Check:

- whether typed arguments are available;
- whether suggestion providers receive permission context;
- whether aliases are first-class;
- whether errors can point to an argument;
- whether command registration changes across supported versions;
- whether asynchronous execution is safe for the project.

## Adapter selection

```text
raw Bukkit/Paper PluginCommand  -> smallest surface, manual parsing; prefer when tree < ~10 leaves
Brigadier (native/mojang-mapped) -> typed args + client-side completion; prefer for complex trees on modern versions
CommandAPI                     -> Brigadier power without NMS; prefer when version range is wide
Cloud                          -> annotation/command model + rich parsers; prefer for large admin surfaces
Skript                         -> script-defined commands; see 14-skript.md
custom dispatcher              -> treat as legacy; wrap behind the AST, migrate outward
```

Record the chosen adapter and its limitations in the AST `implementation` metadata. A limitation constrains implementation; it never silently redefines public semantics.

## Note on 35

The former `35-command-framework-adapters.md` stub is merged into this file. This file (`27`) is the single framework-adapter source.
