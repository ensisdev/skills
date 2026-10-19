# Anti-Exemplar — The Flat God-Root

## Role in this skill

A deliberately bad command tree showing what NOT to build. Study it to recognize the failure modes; never treat any branch as a starting point.

## The bad tree

```text
/myplugin createholo <text...>
/myplugin deleteholo <name>
/myplugin holo2 <name> <line> <text...>     (second syntax for the same edit)
/myplugin tp <anything...>                   (player? coordinates? warp? decided at runtime)
/myplugin all --go                           (bulk teleport, no scope, no confirm)
/myplugin giveadmin <player>                 (op-equivalent, no permission node)
/myplugin reload                             (player-reachable, no capability check)
```

## Why each branch fails

```text
createholo/deleteholo   method-name verbs; lifecycle not separated from mutation (05/22)
holo2                   second canonical path for one meaning; aliases must forward, not fork (law 3)
tp <anything>           direction and target type ambiguous; parse succeeds then fails deep (03/06)
/myplugin all --go      implicit total scope + flag hiding core identity (laws 6/7, 23/34)
giveadmin               privileged execution without capability permission (09/26)
reload on player root   system operation on a player-visible surface (admin-root pattern)
```

## The fix direction (not a template)

One canonical verb per meaning, explicit targets, resource/edit separation, bulk scope with confirm, capabilities behind every mutation, admin surface on its own root. See `patterns/` for the generalized forms.
