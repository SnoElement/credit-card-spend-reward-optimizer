# Credit Card Spend Optimizer — Model

This document describes the assumptions and mappings used across all tools in this repository.

## Valuation Parameters

| Parameter | Default Value | Notes |
|---|---|---|
| Atmos redeemable point value | 0.012 | ¢ per point |
| Status point value | 3000 / 135000 ≈ 0.022222 | Based on tier threshold |
| Hilton point value | 0.004 | ¢ per point |

## Cards

| Card | Reward Type | Notes |
|---|---|---|
| Atmos Summit | Atmos points + status points | Best for Alaska Airlines, dining, foreign |
| Atmos Ascent | Atmos points + status points | Best for Alaska/Hawaiian Airlines, gas, streaming |
| Hawaiian MC (Atmos) | Atmos points + status points | Best for Hawaiian Airlines, gas, dining, groceries |
| Amex Blue Cash Everyday | Cashback | Best for groceries, online retail, gas |
| Amex Hilton Aspire | Hilton points | Best for Hilton stays, flights, dining |
| Disney Premier Visa | Cashback | Best for Disney streaming, gas, groceries, dining |
| Costco Anywhere Visa | Cashback | Best for Costco gas, gas, dining, travel |

## Category Mappings

Each card defines earn rates per spending category. If a category is not explicitly listed for a card, the `other` rate is used as a fallback.

### Canonical Categories

- groceries
- gas
- gas_costco
- dining
- online_retail
- travel_general
- alaska_airlines
- hawaiian_airlines
- foreign
- hilton_stays
- disney_streaming
- costco_general
- other

## Effective Return Calculation

For each card and category:

```
total_value = (atmos_pts * atmos_val) + (status_pts * status_val) + (hilton_pts * hilton_val) + cashback_rate
```

All values are expressed as a decimal (e.g. 0.03 = 3%).