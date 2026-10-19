# Scenario — Scripting Command Systems

## When this scenario applies

Commands are created or routed by Skript, script files, dynamic script registration, or another text-based automation layer.

## Rule

Script implementation does not lower the required command UX standard.

## Forensics

Search:

```text
command /...
aliases:
permission:
trigger:
execute console command
execute player command
make console execute command
make player execute command
```

Also inspect included/shared script files and generated script sources.

## Compatibility

When changing a scripted command, search for command strings in all scripts and config-driven actions.

## Dynamic commands

If scripts create commands from data, document the stable grammar and expose runtime values through completion/help where the platform supports it.

## Error behavior

Differentiate parser errors from domain errors. Avoid silent triggers and ambiguous fallback branches.
