# Scenario — GUI / Menu-Backed Systems

## When this scenario applies

The plugin primarily exposes actions through inventory GUIs, menus or other interactive views, with commands acting as configuration/debug/admin entry points.

## Command role

Do not force every GUI action into a public command. Determine which operations are:

- player-facing and GUI-first;
- useful for command users;
- admin-only setup/configuration;
- internal click actions.

## Integration forensics

Search GUI configs and code for command strings before renaming anything. GUI buttons are compatibility callers.

## Argument design

Commands triggered by GUI/NPC actions should be deterministic and non-interactive. Avoid prompts or hidden context when an action may also be executed by automation.

## Help

Describe command-side entry points separately from GUI navigation so users are not told to use a command for something that only exists in the UI.
