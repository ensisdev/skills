# Scenario — Economy / Shop Systems

## When this scenario applies

The project manages purchasable products, prices, balances, currencies or shop inventories.

## Domain distinctions

Keep these separate:

```text
product identity
price
currency
stock
purchase
sale/refund
catalog membership
```

## Common command design

Frequent player workflows may favor direct verbs:

```text
/shop list
/shop buy <item>
/shop sell <item>
```

Administrative catalog mutation may use a resource namespace:

```text
/shop edit <item> price <amount>
```

## Risk

Economy mutations are financially meaningful. Apply permission and validation; admin bulk changes require explicit scope.

## Amounts

Use a typed numeric/money argument with documented bounds and decimal semantics. Never treat currency as arbitrary text when the implementation has a real amount type.
