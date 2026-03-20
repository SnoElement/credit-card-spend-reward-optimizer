# Credit Card Spend Reward Optimizer

This repository contains tools to compare effective return across multiple credit cards, with parameterized valuations for:

- Atmos redeemable points
- Atmos status points
- Hilton Honors points

You can:

- Use the Python script (`optimizer.py`) to optimize by category
- Use the HTML page (`optimizer.html`) as an interactive calculator
- Use the CSV (`data.csv`) in Excel/Sheets
- Refer to `model.md` for the underlying assumptions and mappings

## Valuation parameters

You can change these three core inputs:

- Atmos redeemable point value (e.g. 0.012)
- Status point value (e.g. 3000 / 135000 ≈ 0.022222222)
- Hilton point value (e.g. 0.004)

These are used consistently across:

- optimizer.py
- optimizer.html
- data.csv

## Categories

Exact category keys currently used in the model:

- alaska_airlines
- car_rentals
- costco_general
- dining
- disney_streaming
- disney_us
- ev_charging
- flights
- foreign
- gas
- gas_costco
- groceries
- hawaiian_airlines
- hilton_stays
- internet_cable
- online_retail
- general
- streaming
- transit
- travel_general

Note: the HTML dropdown exposes a core subset, while the Python optimizer still supports any category key above via the same model and fallback logic.
