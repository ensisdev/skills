# 19 — Canonical Command Vocabulary

## Purpose

Defines semantic distinctions between common verbs. This file extends taxonomy into a decision guide.

## Core distinctions

### create
Introduces a new durable resource.

### add
Appends an item/member/action to an existing collection or sequence.

### insert
Places an item at a meaningful position relative to existing items.

### set
Replaces one known value.

### edit
A namespace for multiple property mutations on one resource.

### update
Use when the project already has an established update/refresh semantic or when the operation is materially different from setting a property. Do not use as a generic synonym for `set`.

### remove
Removes one resource/member/action from its owning context.

### delete
Use only where the domain explicitly uses deletion terminology, compatibility requires it, or the distinction from `remove` is real.

### clear
Empties a collection or resets its contents while preserving the owner/resource.

### reset
Restores a known default/baseline state. It is not a synonym for clear.

### copy / clone
Create another resource based on an existing resource. Select one canonical term and keep the other only as compatibility alias when justified.

### move
Changes the target's spatial position.

### teleport
Teleports an actor. Grammar must make it clear whether the actor is the player or the target resource.

### rotate
Changes orientation without implying position change.

### list
Enumerates resources.

### info
Shows detailed information for a specific resource.

### nearby
Restricts enumeration by spatial proximity.

### find / search
Use for semantic filtering when `list` is insufficient.

### save
Persists runtime state when a manual persistence command is part of the product.

### reload
Re-reads supported configuration/runtime definitions. Do not use it as an undocumented "restart everything" operation.

### convert
Transforms/imports data between formats or supported systems.

## Vocabulary selection rule

If multiple words are technically possible:

1. prefer the project's existing public term;
2. then the domain's natural term;
3. then the canonical terms in this library;
4. use aliases only for compatibility or very strong existing user expectation.

## Ambiguity ban

Avoid generic verbs such as `manage`, `process`, `execute`, `operate`, `perform`, `do` when a concrete domain verb exists.
