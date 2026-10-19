# Scenario — Player Gameplay Systems

## When this scenario applies

Commands are primarily used by players to perform gameplay actions rather than administer persistent resources.

## Design goals

Prioritize:

- short common paths;
- low argument burden;
- clear player-facing vocabulary;
- strong completion;
- useful errors;
- minimal exposure of admin concepts.

## Common pattern

For player workflows, direct domain verbs may be better than a broad `edit` namespace when the action is a frequent gameplay verb.

Example:

```text
/quest start <quest>
/quest abandon <quest>
/kit claim <kit>
```

Do not import admin resource-management patterns just because the feature has stored data internally.

## Permissions

Player commands should default to the smallest capability necessary. Administrative subcommands belong on a separate capability surface when possible.

## Context

Commands using held items, current location or player inventory should explicitly classify themselves as player-only where appropriate.
