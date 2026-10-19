# SKILL SELF-TEST — Guild Bank Feature Dry Run

Validation run: designed a sample feature ("Guild Bank") strictly following this
skill, then scored the result with qa/DESIGN_VALIDATION.md. Purpose: prove the
skill's process is followable end-to-end and find gaps.

---

## Step 1 — Decision order (player goal → … → polish)
- Primary task: deposit/withdraw shared guild items; see balance at a glance.
- Priorities: 1) current contents, 2) my permissions, 3) recent activity.
- Composition family: **utility console** (frequent, low-drama actions).
- Refs chosen: U02 (Settings Rail) + L04 (Grouped Inbox for activity log).
- Borrowed: rail/detail split; grouped log with counts. Changed: rail holds
  member roles, not categories; log groups by day with per-day totals.

## Step 2 — Key design decisions
| Element | Decision |
|---|---|
| Title | `ɢᴜɪʟᴅ ʙᴀɴᴋ` small-cap label + normal section name |
| Layout | left role rail (3 slots), right content grid, no outer frame |
| Deposit | drag-in works natively; no fake "deposit" button |
| Withdraw | right-click item = take one; shift-right = stack (stated in lore footer) |
| Log | last 7 days, collapsed to `▸ Mon · 14 moves`; click expands |
| Empty state | `Depo boş. Bir eşyayı sürükleyip bırak.` |
| Denied state | `Yetersiz yetki — Üye rolü yalnızca bırakabilir.` + required role named |
| Sounds | open=chest open(0.6 vol); confirm=xp pickup; deny=villager no |

## Step 3 — Lint pass (rules/ANTI_PATTERN_LINT.md)
- GLYPH-001 ✅ none · GUI-001 ✅ frameless · PREFIX-001 ✅ standard gradient prefix on all chat
- LORE-001 ✅ two schemas (item lore vs permission info) · DATA-001 ✅ unparsed placeholders
- Result: **0 ERROR, 0 WARN**

## Step 4 — Anti-convergence score vs nearest surface (Market main, EX-01)
composition ✦ typography ✦ iconography ✦ IA ✓ spacing ✦ interaction model ✓ copy ✦ states ✓
**Score: 12/16** → passes deliberate-redesign threshold.

## Step 5 — Validation checklist (DESIGN_VALIDATION.md)
All fast-preflight items pass except one finding: initial design used English-width
assumption in log alignment (`padEnd`) — caught by DATA-002, fixed by switching to
two-component row (label component + value component) instead of padded strings.
**Exception record:** none needed.

## Findings about the skill itself
1. Process is followable without ambiguity. ✔
2. Gap found & fed back: PERFORMANCE_NOTES §2 now referenced from scoreboard-type
   designs; similar note added for log-style surfaces (batch updates).
3. Sound layer integration worked only after SOUND_UX existed — confirmed its value.

Verdict: skill usable as-is; self-test artifact kept as reference output.
