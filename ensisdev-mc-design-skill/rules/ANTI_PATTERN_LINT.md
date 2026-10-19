# Anti-Pattern Lint Rules

Use these as a lightweight design linter before shipping player-facing output.

## Severity levels

- ERROR = violates a core principle and should normally be redesigned
- WARN = suspicious repetition or avoidable noise
- INFO = review opportunity

## Glyph rules

### GLYPH-001
ERROR: Matching decorative glyphs surround a title by default.

Examples:
- `✦ X ✦`
- `★ X ★`
- `◆ X ◆`

### GLYPH-002
WARN: The same decorative glyph is used across many unrelated surfaces.

### GLYPH-003
WARN: Every lore line begins with the same decorative bullet.

### GLYPH-004
INFO: More than two decorative glyphs appear in a compact message cluster.

## Prefix rules

### PREFIX-001
ERROR: A chat message does not start with the standard gradient `[PluginName]` prefix.

### PREFIX-002
WARN: A separator or decorative glyph follows the prefix (`»`, `>>`, `|`, `➜`, `◆`) or sits inside it.

### PREFIX-003
WARN: The prefix is hand-built per message, differs between messages (colors, casing, brackets), or uses more than 3 gradient stops.

### PREFIX-004
INFO: The prefix is repeated on every line of a multi-line message (first line only).

## GUI rules

### GUI-001
ERROR: Every menu uses the same border/filler pattern without functional justification.

### GUI-002
WARN: Navigation slots are cloned across unrelated menus.

### GUI-003
WARN: Center alignment is used for every information class.

### GUI-004
INFO: An empty state has no explanation or next action.

## Lore rules

### LORE-001
ERROR: Every item category uses the same lore schema despite different information needs.

### LORE-002
WARN: Blank lines are used as filler rather than grouping information.

### LORE-003
INFO: Long descriptions use small caps.

## Typography rules

### TYPE-001
WARN: Everything is bold.

### TYPE-002
WARN: Every title uses small caps.

### TYPE-003
INFO: Casing is not intentionally documented for a major feature.

## Color rules

### COLOR-001
ERROR: Semantic states change color meaning across surfaces.

### COLOR-002
WARN: Most elements receive unique colors without hierarchy.

### COLOR-003
INFO: Color is the only signal distinguishing success/error/locked.

## Copy rules

### COPY-001
WARN: Repeated generic phrase such as `Click here` is used for many actions.

### COPY-002
WARN: Repeated generic AI phrase such as `Something went wrong.` appears without recovery guidance.

### COPY-003
INFO: Error lacks a recovery instruction.

## Dynamic content rules

### DATA-001
ERROR: User-provided dynamic content is inserted into MiniMessage markup as trusted formatting.

### DATA-002
WARN: Layout depends on fixed English string width.

### DATA-003
WARN: Long player names/prices are not considered.

## Variety rules

### VAR-001
ERROR: Two major surfaces have interchangeable composition with only text/icon changes.

### VAR-002
WARN: More than three recent surfaces share the same title strategy.

### VAR-003
INFO: New surface did not intentionally vary at least three appropriate design dimensions.

## Compatibility rules

### COMPAT-001
WARN: Legacy `§` codes, `ChatColor` or `translateAlternateColorCodes` used instead of MiniMessage/Adventure.

## Turkish copy rules

### TR-001
WARN: A small-caps word mixes in normal `ç ğ ö ş ü` (for example `sᴀᴛış`). Use normal case or a synonym. See `references/TURKISH_COPY.md`.

### TR-002
WARN: No-arg `toUpperCase()` / `toLowerCase()`. Use `Locale.ROOT` for identifiers and the player's locale for display text.

## Mechanical checking

`tools/lint_messages.py` implements PREFIX-001..003, GLYPH-001, GLYPH-004, LORE-003, DATA-001, DATA-002, COMPAT-001, TR-001, TR-002 as line-based heuristics. All other rules need judgment (see `qa/DESIGN_VALIDATION.md`).

