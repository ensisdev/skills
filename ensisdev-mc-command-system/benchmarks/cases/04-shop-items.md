# Case 04 — Shop Items

## Problem

A shop plugin mixes player purchase flow with admin catalog editing on one root: `/shop buy`, `/shop sell`, `/shop additem`, `/shop setprice`, `/shop removeitem`. Prices are decimals with per-item currency. Untangle the two audiences while keeping `/shop buy <item>` stable for documented player guides.

## Scenarios

`economy-shop`, `gameplay-player`.

## Input fixtures (OBSERVED)

```java
// ShopService (observed, simplified)
shop.buy(player, item);
shop.setPrice(item, amount, currency);
catalog.remove(item);
```

```text
# docs/players.md (observed)
Buy with /shop buy <item>, sell with /shop sell <item>.
```

## Journeys

1. list → buy (confirm with price) → success;
2. admin sets price → player-visible price updates;
3. invalid amount (`abc`, negative) → usage/domain error, nothing charged.

## Pass criteria

Player verbs direct, admin mutations in resource/edit namespace or admin tier; typed money argument with bounds per economy-shop scenario; purchase is confirmed with named cost per 49; catalog removal risk-classed.
