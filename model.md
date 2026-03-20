# Credit Card Spend Reward Model

This document defines the value model used by the optimizer tools.

## Objective

For a selected spend category, compute the effective value return for each card and rank cards from highest to lowest total value.

## Inputs

The model uses three configurable point valuations:

- Atmos redeemable point value: default `0.012`
- Atmos status point value: default `3000 / 135000 = 0.0222222222`
- Hilton Honors point value: default `0.004`

Cashback values are already represented as direct decimal return rates and do not require conversion.

## Core Formula

For a card and category:

- `atmos_value = atmos_points_rate * atmos_point_value`
- `status_value = status_points_rate * status_point_value`
- `hilton_value = hilton_points_rate * hilton_point_value`
- `cash_value = cashback_rate`

Total effective return:

- `total_value = atmos_value + status_value + hilton_value + cash_value`

The command-line output multiplies each component by `100` to display percentages.

## Category Lookup Rule

When retrieving any rate (Atmos points, status points, Hilton points, or cashback):

1. If the selected category exists for that card and reward type, use that rate.
2. Else, if a `general` fallback exists for that card and reward type, use `general`.
3. Else, use `0`.

This fallback behavior comes from `get_rate(...)` in the optimizer implementation.

## Cards and Rate Tables

All rates below are copied from the model in `optimizer.py` and `optimizer.html`.

### Atmos Summit

- Atmos points:
	- `alaska_airlines: 3`
	- `hawaiian_airlines: 3`
	- `dining: 3`
	- `foreign: 3`
	- `general: 1`
- Status points:
	- `general: 0.5`

### Atmos Ascent

- Atmos points:
	- `alaska_airlines: 3`
	- `hawaiian_airlines: 3`
	- `ev_charging: 2`
	- `gas: 2`
	- `transit: 2`
	- `internet_cable: 2`
	- `streaming: 2`
	- `general: 1`
- Status points:
	- `general: 0.3333333333`

### Hawaiian MC (Atmos)

- Atmos points:
	- `alaska_airlines: 3`
	- `hawaiian_airlines: 3`
	- `gas: 2`
	- `dining: 2`
	- `groceries: 2`
	- `general: 1`
- Status points:
	- `general: 0.3333333333`

### Amex Blue Cash Everyday

- Cashback:
	- `groceries: 0.03`
	- `online_retail: 0.03`
	- `gas: 0.03`
	- `general: 0.01`

### Amex Hilton Aspire

- Hilton points:
	- `hilton_stays: 14`
	- `flights: 7`
	- `car_rentals: 7`
	- `dining: 7`
	- `general: 3`

### Disney Premier Visa

- Cashback:
	- `disney_streaming: 0.05`
	- `gas: 0.02`
	- `groceries: 0.02`
	- `dining: 0.02`
	- `disney_us: 0.02`
	- `general: 0.01`

### Costco Anywhere Visa

- Cashback:
	- `gas_costco: 0.05`
	- `gas: 0.04`
	- `dining: 0.03`
	- `travel_general: 0.03`
	- `costco_general: 0.02`
	- `general: 0.01`

## Notes on Category Coverage

Not all categories are present in every interface list. The optimizer still handles any category string because rates fall back to each card's `general` category when a specific category is missing.

Examples of categories used in card definitions but not always exposed in every UI selector:

- `ev_charging`
- `transit`
- `internet_cable`
- `streaming`
- `flights`
- `car_rentals`
- `disney_us`

## Practical Interpretation

- The model is an effective-value comparison, not a statement of guaranteed cash redemption.
- Results are sensitive to the three point valuation assumptions.
- If your personal valuation changes, rerun the optimizer with updated inputs to get a new ranking.
