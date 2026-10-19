# 21 — Command Journey Testing

## Purpose

Tests commands as user workflows rather than isolated parser functions.

## Journey format

```yaml
journey:
  goal: "..."
  actor: player|admin|console|automation
  starting_knowledge: none|basic|expert
  steps:
    - input: "/root"
      expected_discovery: "..."
    - input: "/root subcommand ..."
      expected: "..."
  failure_recovery:
    invalid_input: "..."
    missing_permission: "..."
```

## Mandatory journeys

### First discovery
Can a new user discover the operation from the root and completion/help?

### Common workflow
Can the dominant user goal be completed without unnecessary navigation?

### Mutation recovery
What happens when a value is invalid? Does the error identify the argument and expected shape?

### Permission denial
Does the user receive a useful denial without leaking protected resource information?

### Console workflow
Where supported, can console use the operation without player-only assumptions?

### Completion journey
At each cursor position, are only valid next choices suggested?

### Destructive workflow
Is destructive intent obvious? Is confirmation/selectivity appropriate?

### Compatibility journey
Does an old documented command continue to work or receive a clear migration path?

## Journey quality defects

A journey is defective when:

- the next step is not discoverable;
- the command requires knowledge that help/completion does not expose;
- an error gives no recovery path;
- the actor context is ambiguous;
- a common goal passes through internal implementation concepts.

## Output

```text
JOURNEY: PASS | PASS WITH NOTES | FAIL
Goal: ...
Actor: ...
Failure point: ...
Recovery quality: ...
```
