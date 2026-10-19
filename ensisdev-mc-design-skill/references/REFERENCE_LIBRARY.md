# REFERENCE LIBRARY — 45 REAL COMPOSITION REFERENCES

Conceptual references for player-facing Minecraft surfaces. Each reference is an
information architecture plus its signature techniques. Combine 2–4 references from
different families; never copy one wholesale. Record what you borrowed and what you
changed (see SKILL.md → Reference usage).

Legend: **Focus** = what the composition optimizes · **Use for** = fitting surfaces ·
**Key technique** = the defining move · **Avoid** = the failure mode · **Variation cue**
= how to diverge when using it repeatedly.

---

## Family E — Editorial

### REF-E01 — Magazine Cover
- **Focus:** one dominant headline, everything else subordinate.
- **Use for:** event announcements, season openers, main menu hero panels.
- **Key technique:** single oversized title + one supporting stat line + one CTA.
- **Avoid:** competing headings of equal size.
- **Variation cue:** swap dominant element between title, artwork slot, and stat.

### REF-E02 — Newspaper Column
- **Focus:** dense scannable columns with strong section rules.
- **Use for:** changelogs, patch notes, news boards.
- **Key technique:** thin horizontal rules between sections, no borders around boxes.
- **Avoid:** boxed cards for every section.
- **Variation cue:** vary column count (1 vs 2) and rule placement.

### REF-E03 — Table of Contents
- **Focus:** numbered index that promises what each section contains.
- **Use for:** help menus, guide hubs, quest journals.
- **Key technique:** `01 ᴏᴠᴇʀᴠɪᴇᴡ …… p.2` style leader lines with page/slot pointers.
- **Avoid:** unnumbered walls of links.
- **Variation cue:** leaders vs indentation vs numbered chips.

### REF-E04 — Pull Quote
- **Focus:** one highlighted statement breaking a quiet layout.
- **Use for:** motivational onboarding, NPC dialog emphasis, milestone moments.
- **Key technique:** centered italic/accent line surrounded by generous whitespace.
- **Avoid:** pulling more than one quote per screen.
- **Variation cue:** left-rule quote vs centered vs oversized quotation glyph.

### REF-E05 — Sidebar Annotation
- **Focus:** primary content with margin notes for metadata.
- **Use for:** item detail views, player profiles with side stats.
- **Key technique:** main column carries narrative; right column carries `ᴅᴀᴛᴇ / ᴛᴀɢs / sᴛᴀᴛᴜs`.
- **Avoid:** letting margin notes outnumber content lines.
- **Variation cue:** annotation side, density, label casing.

### REF-E06 — Chapter Divider
- **Focus:** transitional screen marking a mode change.
- **Use for:** wizard steps, realm switches, tutorial phase intros.
- **Key technique:** roman numeral or stage number + short subtitle, nothing else.
- **Avoid:** stuffing navigation onto a divider.
- **Variation cue:** numbering system, alignment, accent placement.

---

## Family D — Dashboard

### REF-D01 — KPI Row
- **Focus:** top strip of 3–5 headline numbers before any detail.
- **Use for:** economy overview, faction stats, server dashboards.
- **Key technique:** large value + tiny muted label pairs, consistent width slots.
- **Avoid:** decorating the numbers with per-value different colors.
- **Variation cue:** value-first vs label-first ordering; separator style.

### REF-D02 — Sparkline Card
- **Focus:** trend at a glance inside a compact card.
- **Use for:** balance history, playtime trends, market price movement.
- **Key technique:** mini block-character chart (`▁▃▅▂▇`) + delta (`▲ 12%`).
- **Avoid:** full-width charts stealing the detail view's job.
- **Variation cue:** chart height, delta position, card grouping.

### REF-D03 — Bento Grid
- **Focus:** asymmetric tiles sized by importance.
- **Use for:** hub menus mixing stats, shortcuts, and live events.
- **Key technique:** one double-width tile anchors the grid; others fill around it.
- **Avoid:** uniform equal tiles (that is a plain grid, not bento).
- **Variation cue:** which tile is anchor; tile aspect ratios.

### REF-D04 — Leaderboard Podium
- **Focus:** rank 1–3 visually elevated, table below.
- **Use for:** top players, richest balances, event winners.
- **Key technique:** podium row with medal semantics, then compact ranked rows.
- **Avoid:** identical styling for every row including #1.
- **Variation cue:** podium representation (slots vs text), row density.

### REF-D05 — Gauge Cluster
- **Focus:** multiple related meters read as one instrument panel.
- **Use for:** machine status, resource rates, kit readiness.
- **Key technique:** aligned meters sharing one scale vocabulary and unit style.
- **Avoid:** mixed bar styles in the same cluster.
- **Variation cue:** meter form (blocks, percentage, stages) kept constant per cluster.

### REF-D06 — Ticker Strip
- **Focus:** horizontally scrolling/streaming compact updates.
- **Use for:** recent sales feed, live auction pings.
- **Key technique:** one-line entries, newest emphasized, older muted.
- **Avoid:** multi-line entries breaking rhythm.
- **Variation cue:** recency encoding via opacity-analog (color depth) vs prefix marker.

---

## Family U — Utility / Console

### REF-U01 — Command Palette
- **Focus:** one input concept, filtered results beneath.
- **Use for:** admin tools, teleport search, item finders.
- **Key technique:** search-slot at top, live-filtered list below, `no matches → suggestion` state.
- **Avoid:** burying the input below branding.
- **Variation cue:** filter style (chips vs text), result row anatomy.

### REF-U02 — Settings Rail
- **Focus:** left category rail + right detail pane.
- **Use for:** settings, kit configuration, permission editors.
- **Key technique:** rail items are nouns; detail pane shows current value + toggle/stepper.
- **Avoid:** mixing actions into the rail.
- **Variation cue:** rail width, selection marker, value control form.

### REF-U03 — Checklist Console
- **Focus:** tasks with explicit done/pending states.
- **Use for:** setup wizards, daily missions, claimable rewards.
- **Key technique:** `✓` prefix for complete, hollow marker for pending, action verb on ready items.
- **Avoid:** color-only completion signaling.
- **Variation cue:** marker glyph family, ordering (done-first vs priority-first).

### REF-U04 — Toggle Board
- **Focus:** grid of binary switches with instant feedback.
- **Use for:** notification preferences, module switches.
- **Key technique:** each cell = label + ON/OFF word, never color alone.
- **Avoid:** icon-only toggles.
- **Variation cue:** switch wording, cell size, grouping.

### REF-U05 — Maintenance Panel
- **Focus:** system state honesty during downtime/restricted mode.
- **Use for:** disabled features, restart notices.
- **Key technique:** state word + expected recovery time + what still works.
- **Avoid:** hiding working features without explanation.
- **Variation cue:** severity tone, information order.

### REF-U06 — Log Stream
- **Focus:** reverse-chronological operational entries.
- **Use for:** transaction history, moderation logs.
- **Key technique:** timestamp + actor + action in fixed column rhythm; hover reveals raw detail.
- **Avoid:** prose paragraphs per entry.
- **Variation cue:** column order, grouping by day vs continuous.

---

## Family A — Detail + Action

### REF-A01 — Product Page
- **Focus:** one object dominates; actions flank it.
- **Use for:** item details, listing views, pet/mount cards.
- **Key technique:** identity block top-left, price/action block bottom-right, specs between.
- **Avoid:** actions competing with title for first glance.
- **Variation cue:** action block placement, spec density.

### REF-A02 — Receipt Confirmation
- **Focus:** post-transaction verification of exactly what happened.
- **Use for:** purchase confirmations, trade summaries.
- **Key technique:** line-item ledger + total + undo window countdown.
- **Avoid:** celebratory noise drowning the numbers.
- **Variation cue:** ledger alignment, undo affordance.

### REF-A03 — Preview Pane
- **Focus:** see the result before committing.
- **Use for:** kit previews, skin previews, upgrade outcomes.
- **Key technique:** before/after or "you will receive" mock slot arrangement.
- **Avoid:** requiring commit to reveal the outcome.
- **Variation cue:** static preview vs interactive sample.

### REF-A04 — Danger Zone
- **Focus:** destructive action isolated with friction.
- **Use for:** deletion, resets, guild disbanding.
- **Key technique:** separated zone, typed/click-twice confirmation, consequence sentence.
- **Avoid:** placing danger next to routine actions.
- **Variation cue:** friction type, wording tone.

### REF-A05 — Inspector Card
- **Focus:** hovering/selecting an entry updates a persistent side card.
- **Use for:** auction lists with detail card, player inspectors.
- **Key technique:** list stays stable; card mirrors selection instantly.
- **Avoid:** full-screen navigation for every peek.
- **Variation cue:** card position, update trigger.

---

## Family W — Progressive Flow

### REF-W01 — Stepper Header
- **Focus:** visible progress across 3–6 steps.
- **Use for:** creation wizards, listings, setup flows.
- **Key technique:** `1 ─ 2 ─ 3` progress markers, current step emphasized, future steps dimmed.
- **Avoid:** hiding total step count.
- **Variation cue:** stepper position and visual form.

### REF-W02 — One Question Screen
- **Focus:** single decision per screen.
- **Use for:** critical choices, tutorials, confirmations mid-flow.
- **Key technique:** question as title, two contrasting answers, no extra chrome.
- **Avoid:** stacking unrelated questions.
- **Variation cue:** answer layout, supporting hint presence.

### REF-W03 — Guided Tour Bubble
- **Focus:** pointing annotation over a live surface.
- **Use for:** feature discovery, first-run hints.
- **Key technique:** highlight target region + short explanation + "got it" dismiss.
- **Avoid:** tour longer than 5 stops.
- **Variation cue:** pointer style, pacing (auto vs manual).

### REF-W04 — Checkpoint Resume
- **Focus:** returning users continue where they stopped.
- **Use for:** multi-session quests, partial applications.
- **Key technique:** resume banner with saved state summary + continue CTA + restart link.
- **Avoid:** forcing restart to reach resume.
- **Variation cue:** banner placement, restart prominence.

---

## Family L — List + Filter

### REF-L01 — Catalog Grid
- **Focus:** uniform browsable cards with stable scanning rhythm.
- **Use for:** item shops, cosmetic galleries, warp menus.
- **Key technique:** fixed card anatomy (name, one metric, state), page footer with position indicator.
- **Avoid:** per-card layout improvisation.
- **Variation cue:** card anatomy order, empty-slot treatment.

### REF-L02 — Filter Chips Bar
- **Focus:** visible active filters above the list.
- **Use for:** auction searches, quest categories.
- **Key technique:** chips show `category: value`; active chip removable; result count updates live.
- **Avoid:** hidden filters only reachable through settings.
- **Variation cue:** chip density, placement (top vs rail).

### REF-L03 — Sorted Table
- **Focus:** comparable rows under sortable column headers.
- **Use for:** market listings, player rankings, price comparison.
- **Key technique:** header shows sort direction; numbers right-aligned; units in header not per-cell.
- **Avoid:** mixed alignment across numeric columns.
- **Variation cue:** default sort, column set.

### REF-L04 — Grouped Inbox
- **Focus:** items clustered by day/type/sender with sticky group headers.
- **Use for:** mailboxes, notifications, claim queues.
- **Key technique:** group header carries count + bulk action; items stay terse.
- **Avoid:** flattening groups when count is high.
- **Variation cue:** grouping dimension, header action set.

### REF-L05 — Infinite Shelf
- **Focus:** continuous scroll feel within inventory pagination limits.
- **Use for:** large catalogs where pages would fragment browsing.
- **Key technique:** bottom row = "load more" semantics with remaining-count, not page numbers.
- **Avoid:** fake infinite scroll that actually jumps pages silently.
- **Variation cue:** load-more wording, progress hint.

---

## Family S — Status Console

### REF-S01 — Vital Signs Board
- **Focus:** everything OK at one glance; anomalies pop.
- **Use for:** server status, faction resources, machine grids.
- **Key technique:** all-normal = quiet; any anomaly gets the only accent color + label.
- **Avoid:** celebratory green everywhere drowning real alerts.
- **Variation cue:** anomaly encoding (icon vs color vs label).

### REF-S02 — Cooldown Ring
- **Focus:** waiting made tangible and fair.
- **Use for:** ability cooldowns, kit timers, tax windows.
- **Key technique:** remaining time as primary value; ready-state flips emphasis to the action verb.
- **Avoid:** hiding readiness behind a color flip only.
- **Variation cue:** time format, ready announcement channel.

### REF-S03 — Live Event Banner
- **Focus:** time-boxed event state with urgency without panic.
- **Use for:** double-XP weekends, world bosses.
- **Key technique:** event name + phase (`starting / live / final 5 min`) + compact CTA.
- **Avoid:** permanent-looking banners for temporary events.
- **Variation cue:** urgency ramp styling, CTA evolution by phase.

### REF-S04 — Queue Position
- **Focus:** transparent waiting with movement feedback.
- **Use for:** matchmaking, ticket systems, transfer queues.
- **Key technique:** position number + estimated wait + what speeds it up.
- **Avoid:** static "please wait" with no motion signal.
- **Variation cue:** estimate honesty level, reassurance copy.

---

## Family C — Comparison

### REF-C01 — Side-by-Side Delta
- **Focus:** two states aligned row-by-row with deltas.
- **Use for:** upgrade previews, gear comparisons, plan tiers.
- **Key technique:** shared row labels center; left/right values; delta column colored semantically.
- **Avoid:** comparing more than three options at once.
- **Variation cue:** delta representation, winner marking.

### REF-C02 — Before → After Story
- **Focus:** transformation narrative rather than table.
- **Use for:** prestige upgrades, rebirth systems.
- **Key technique:** `now` paragraph → arrow → `then` paragraph, only changed attributes bolded.
- **Avoid:** restating unchanged stats.
- **Variation cue:** arrow treatment, bold discipline.

### REF-C03 — Trade Offer Mirror
- **Focus:** both sides of an exchange face each other symmetrically.
- **Use for:** trading, barter, guild contributions.
- **Key technique:** your side vs their side with center divider; fairness summary line at bottom.
- **Avoid:** asymmetric emphasis implying bias.
- **Variation cue:** divider form, fairness visualization.

### REF-C04 — Tier Ladder
- **Focus:** vertical progression of levels with current position marked.
- **Use for:** rank systems, battle passes, donor tiers.
- **Key technique:** rungs share anatomy; current rung expanded to show next-unlock detail.
- **Avoid:** equal expansion of every rung.
- **Variation cue:** expansion behavior, ladder orientation.

---

## Family M — Commerce

### REF-M01 — Price-First Listing
- **Focus:** cost dominates; product identity second.
- **Use for:** bulk markets, stock exchanges, commodity shops.
- **Key technique:** large price numeral, small item caption, seller tertiary or hidden.
- **Avoid:** decorative frames competing with numerals.
- **Variation cue:** currency symbol handling, discount display.

### REF-M02 — Seller Stall
- **Focus:** shop identity and curation personality.
- **Use for:** player shops, guild vendors.
- **Key technique:** stall header (name + rating) above curated rows; a personal note is allowed.
- **Avoid:** template sameness between different sellers.
- **Variation cue:** identity block richness, curation ordering.

### REF-M03 — Checkout Ledger
- **Focus:** pre-purchase arithmetic transparency.
- **Use for:** cart views, bulk purchases, fee disclosure.
- **Key technique:** subtotal → fees → total ladder; confirm button states the exact charge.
- **Avoid:** surprise fees after confirm.
- **Variation cue:** breakdown depth, button copy.

### REF-M04 — Stock Level Signal
- **Focus:** scarcity communicated honestly.
- **Use for:** limited stock, flash sales.
- **Key technique:** remaining count as data (`3 left`), optional subtle depletion meter; no fake countdowns.
- **Avoid:** manufactured urgency decorations.
- **Variation cue:** scarcity threshold styling, restock note.

### REF-M05 — Transaction History Card
- **Focus:** personal commerce memory.
- **Use for:** my-purchases, my-sales tabs.
- **Key technique:** direction arrow + counterpart + signed amount + status chip; click reveals receipt (REF-A02).
- **Avoid:** mixing incoming/outgoing without directional markers.
- **Variation cue:** entry anatomy order, chip vocabulary.

### REF-M06 — Wishlist Watch
- **Focus:** tracked items with condition-change alerts.
- **Use for:** price watches, restock alerts, saved builds.
- **Key technique:** target condition stated (`under 500c`); current vs target shown; alert toggle inline.
- **Avoid:** silent wishlist with no trigger explanation.
- **Variation cue:** condition display, alert surface choice.

---

## Usage protocol

1. Select the family matching the player's task (see `rules/REFERENCE_PATTERNS.md`).
2. Pick 2–4 references from *different* families; note their IDs.
3. Write down: borrowed concept · deliberate change · plugin-specific constraint.
4. Run anti-convergence check against the plugin's nearest existing screens.
5. If two recent surfaces used the same reference unchanged, vary at least three dimensions or pick a different reference.



