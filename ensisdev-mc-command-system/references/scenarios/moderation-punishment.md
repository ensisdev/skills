# Scenario — Moderation and Punishment Systems

## When this scenario applies

The project disciplines players: warns, mutes, kicks, temp-bans, bans, history lookup, appeals-adjacent inspection.

## Domain distinctions

Keep these separate:

```text
offense record (warn, note)
restriction (mute, freeze)
removal (kick, temp-ban, ban)
inspection (history, check, alts)
reversal (unmute, unban, pardon)
```

## Common command design

Moderation favors explicit-target direct verbs with duration/reason arguments:

```text
/warn <player> <reason>
/mute <player> [duration] [reason]
/ban <player> [duration] [reason]
/history <player>
/unban <player>
```

Durations are typed arguments with documented units (`30m`, `2d`, `perm`), never bare integers with implicit units.

## Risk

Moderation commands are `mutate` minimum, `destructive` for bans (reputation/state loss) and `bulk-destructive` for range/IP actions. Apply 23/34 strictly:

- every action logs actor, target, reason, duration, timestamp;
- reasons are required, not optional — reasonless punishment is a design defect;
- bulk actions (IP-ban, range-ban) need explicit scope + confirmation;
- `history` is read but permission-gated: completion must not leak other players' records (11).

## Reversibility

Every restrictive verb has a documented reverse verb at the same permission tier or higher. Time-based expiry states its clock source (server time, playtime) in help.
