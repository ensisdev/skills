# 10 — Player, Admin and Console UX

## Purpose

Separates command surfaces by user context.

## Player UX

Optimize for:

- short common paths;
- obvious nouns/verbs;
- useful defaults;
- low argument count;
- completion that reveals legal choices;
- errors that teach the next step.

## Administrator UX

Optimize for:

- precise targeting;
- inspection tools;
- filters/sorting;
- safe bulk operations;
- detailed property control;
- predictable permissions.

Do not hide critical administration behind an intentionally abbreviated player command if it harms manageability.

## Console UX

Console lacks:

- player location;
- player identity unless provided;
- interactive world context.

Commands should declare console compatibility explicitly.

If a command is useful from both player and console, keep the semantic command the same and supply a non-ambiguous location/selector form for console use.

## Context-aware aliases

Do not create different words for the same operation merely because one user is a player and another is an administrator. Prefer the same semantic command with different permissions unless the workflows genuinely differ.

## Message audience

Player feedback should be concise. Admin feedback can include identifiers, state and diagnostic details. Console output should be log-friendly and unambiguous.
