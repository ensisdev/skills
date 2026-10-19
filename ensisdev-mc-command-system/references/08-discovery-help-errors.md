# 08 — Discovery, Help and Errors

## Purpose

Defines how users discover command capabilities and recover from mistakes.

## Help design

Help should answer, in order:

1. what can I do;
2. what does this command operate on;
3. what arguments exist;
4. which commands are available to my permission level.

Use paginated help for large trees.

## Contextual help

Prefer contextual help:

```text
/root edit
/root edit <resource>
/root action <resource> <trigger>
```

The closer help is to the user's current cursor/command context, the more useful it is.

## Error taxonomy

### Parse error
User supplied an invalid type/format.

Say what type/value is expected.

### Selection error
Target resource, player or world does not exist.

Name the failed selector.

### Permission error
Do not reveal sensitive administrative details. Provide the permission denial message appropriate to the project.

### State error
The resource exists but the operation is currently invalid.

Explain the state conflict.

### Capability error
The selected resource type does not support the requested property/action.

Say what is supported when helpful.

## Error message quality

Bad:

```text
Invalid.
```

Better:

```text
Unknown NPC 'guide'. Use /npc list to view available NPCs.
```

Best when appropriate:

```text
NPC 'guide' was not found. Available matches: guide_main, guide_spawn.
```

## Confirmation

Confirmation should be reserved for operations with meaningful destructive or broad effects. Avoid confirmation spam on normal single-resource edits.
