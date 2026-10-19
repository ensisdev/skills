# 47 — Proxy and Network Commands

## Purpose

Covers command surfaces that cross server boundaries: BungeeCord/Velocity proxy commands and backend commands that assume proxy context.

## Separation rule

Proxy commands and backend commands are different contracts even when names match. A backend `/server lobby` and a proxy `/server lobby` have different actors, permissions and failure modes. Model them as separate AST roots with a `network` note; never merge into one tree by name coincidence.

## Proxy-side design

- Keep proxy roots few and stable (`server`, `hub`, `msg`, `party`): they are typed blind (no tab data from backends by default) and hard to migrate.
- Backend server names are data, not syntax: `/server <name>` completes from the proxy's server list, never from a hardcoded enum.
- Cross-server actions (`kick`, `ban`, `tp`) need explicit scope: which server, and whether the effect is local or network-wide. Default to local; network-wide requires `bulk-destructive` controls (23/34).
- Proxy permissions live in the proxy, not in backend LuckPerms contexts. Document where each node is evaluated.

## Backend awareness

When a backend command behaves differently under a proxy (e.g. `/list` should show network count, `/msg` should route cross-server):

```text
explicit variant wins: /msg (local) vs /amsq (network) is clearer than context-dependent /msg
fallback must be documented: what happens when the proxy channel is down
no silent cross-talk: a backend command must never message another server without user-visible indication
```

## Forensics signals

```text
ProxyServer
PluginMessageListener
BungeeCord channel / velocity messaging
PlayerServerConnectedEvent
/server
```

## AST record

```yaml
contexts: [player]
network:
  executed_on: proxy        # proxy | backend | either
  scope: network            # local | network
  fallback: local-only with warning
```
