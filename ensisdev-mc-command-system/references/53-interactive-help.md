# 53 — Interactive Help and Chat UX

## Purpose

Designs help, lists and errors as interactive chat UI (Adventure components), not walls of text. On modern Paper, the help surface is clickable; static `/help` dumps are the fallback, not the design.

## Component vocabulary

Use exactly these interaction shapes; do not invent new ones per leaf:

```text
command button    click runs / suggests the command (RUN_COMMAND / SUGGEST_COMMAND)
hover detail      hover shows cost, permission tier, or destination info
page control      [← Prev] [page n/m] [Next →] for lists over one screen
inline fix        error message carries a clickable correction (e.g. Did you mean /warp go spawn?)
confirm button    destructive prompt with [Confirm] [Cancel] components (see 49)
```

## Help layout (one root)

```text
/aqua Warps /gray (page 1/2) — click a warp to travel
  / hover: <name> — <cost> — cooldown <duration>
/warp go <name>
/warp list [--page n]
/warpadmin create <name>  /gray (admin)
```

Rules:

- One screen max per page (~8 content lines + footer). Overflow goes to pages, never to scrollback.
- Every displayed command is clickable with the correct click action: safe reads use RUN_COMMAND; destructive/charged paths use SUGGEST_COMMAND so the player reviews before executing.
- Admin-only paths render only for viewers with the capability (same filter as completion, 11/26).
- Hover text answers "what happens if I click this" — cost, target, irreversibility.

## Errors as UI

Map the 08 taxonomy to components:

```text
usage error    red usage line + clickable correct-syntax suggestion
domain error   yellow state explanation + inline fix button where a fix exists
permission     generic gray denial, no buttons, no structure leak
cooldown/cost  remaining wait / balance with a [Back] or [List] navigation button
```

## Fallback contract

When Adventure is unavailable (old versions per 46, console, RCON), the same AST leaf renders as plain text with identical information order. Interactive components are progressive enhancement; information must never live only in a hover.

## Locale interaction

Component skeletons (buttons, pagination) use locale keys like any text (48). Click actions reference canonical paths, never display text — translated labels must not break the command being run.
