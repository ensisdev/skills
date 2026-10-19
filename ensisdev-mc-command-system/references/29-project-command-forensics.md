# 29 — Project Command Forensics

## Purpose

Defines how to discover the real command surface of a repository before redesign.

## Registration search

Search for:

```text
onCommand
CommandExecutor
TabCompleter
CommandSender
CommandContext
Brigadier
CommandDispatcher
LiteralArgumentBuilder
RequiredArgumentBuilder
CommandAPI
Cloud
registerCommand
registerCommands
plugin.yml
paper-plugin.yml
commands:
```

## Invocation search

Search for:

```text
dispatchCommand
performCommand
executeCommand
console command
player command
make console execute command
make player execute command
command strings
```

## Public surface search

Search:

```text
README
/docs
/wiki
examples
messages
help
usage
alias
permission
```

## Integration search

Look for command strings or command builders inside:

- GUIs;
- NPC definitions;
- hologram actions;
- scheduled tasks;
- Skript;
- placeholder integrations;
- config-driven actions;
- tests.

## Resource and permission search

Identify command-facing registries and permission constants. Distinguish observed permission nodes from merely proposed nodes.

## Output

```yaml
forensics:
  roots: []
  registration_locations: []
  completion_locations: []
  permission_locations: []
  direct_invocations: []
  documentation_refs: []
  integration_refs: []
  tests: []
  compatibility_hotspots: []
```

## Rule

A command is part of the compatibility surface if code, scripts, integrations or public documentation can reasonably invoke it, even if the command implementation itself is small.
