# Case 12 — Localized Help and Errors

## Problem

A plugin hardcodes English strings in handlers, mixes MiniMessage with legacy `&` codes, and interpolates player-supplied names unescaped (a warp named `<red>` recolors output). Design the locale contract: keys per leaf, fallback bundle, escaping rule, and error taxonomy mapping.

## Scenarios

`gameplay-player`, `admin-maintenance`.

## Input fixtures (OBSERVED)

```java
// WarpCommands (observed, simplified)
sender.sendMessage("&aWarp " + name + " created!");
sender.sendMessage("<red>Unknown warp " + input + "</red>");
```

## Journeys

1. create warp named `<red>oops` → name renders literally, no color leak;
2. Turkish client with missing `tr` key → falls back to `en`, no raw key shown;
3. usage error highlights the bad argument; domain error states state; permission denial is generic.

## Pass criteria

Locale keys per leaf per 48 with complete fallback bundle; user input escaped; MiniMessage vs plain-text arguments declared; canonical verbs stay English with no speculative alias trees.
