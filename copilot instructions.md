Here it is — the **cleaned, Copilot‑friendly combined Markdown bundle**.  
Paste this entire thing into a single file in your GitHub repo (e.g., `bundle.md`).  
GitHub Copilot will immediately recognize each fenced block and offer to **create the corresponding files automatically**.

---

# 📦 **CREDIT CARD SPEND OPTIMIZER — FILE BUNDLE**  
*(Cleaned version, Copilot‑ready)*

---

# README.md
```md
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

Canonical categories used in the model:

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

You can extend these as needed.
```

---

# optimizer.py
```python
from dataclasses import dataclass
from typing import Dict, List, Tuple
import sys

@dataclass
class Card:
    name: str
    atmos_points: Dict[str, float]
    status_points: Dict[str, float]
    hilton_points: Dict[str, float]
    cashback: Dict[str, float]

def get_rate(mapping: Dict[str, float], category: str) -> float:
    if category in mapping:
        return mapping[category]
    if "other" in mapping:
        return mapping["other"]
    return 0.0

cards: List[Card] = [
    Card(
        name="Atmos Summit",
        atmos_points={"alaska_airlines": 3, "dining": 3, "foreign": 3, "other": 1},
        status_points={"other": 0.5},
        hilton_points={},
        cashback={},
    ),
    Card(
        name="Atmos Ascent",
        atmos_points={
            "alaska_airlines": 3,
            "hawaiian_airlines": 3,
            "ev_charging": 2,
            "gas": 2,
            "transit": 2,
            "internet_cable": 2,
            "streaming": 2,
            "other": 1,
        },
        status_points={"other": 0.3333333333},
        hilton_points={},
        cashback={},
    ),
    Card(
        name="Hawaiian MC (Atmos)",
        atmos_points={
            "hawaiian_airlines": 3,
            "gas": 2,
            "dining": 2,
            "groceries": 2,
            "other": 1,
        },
        status_points={"other": 0.3333333333},
        hilton_points={},
        cashback={},
    ),
    Card(
        name="Amex Blue Cash Everyday",
        atmos_points={},
        status_points={},
        hilton_points={},
        cashback={
            "groceries": 0.03,
            "online_retail": 0.03,
            "gas": 0.03,
            "other": 0.01,
        },
    ),
    Card(
        name="Amex Hilton Aspire",
        atmos_points={},
        status_points={},
        hilton_points={
            "hilton_stays": 14,
            "flights": 7,
            "car_rentals": 7,
            "dining": 7,
            "other": 3,
        },
        cashback={},
    ),
    Card(
        name="Disney Premier Visa",
        atmos_points={},
        status_points={},
        hilton_points={},
        cashback={
            "disney_streaming": 0.05,
            "gas": 0.02,
            "groceries": 0.02,
            "dining": 0.02,
            "disney_us": 0.02,
            "other": 0.01,
        },
    ),
    Card(
        name="Costco Anywhere Visa",
        atmos_points={},
        status_points={},
        hilton_points={},
        cashback={
            "gas_costco": 0.05,
            "gas": 0.04,
            "dining": 0.03,
            "travel_general": 0.03,
            "costco_general": 0.02,
            "other": 0.01,
        },
    ),
]

def value_for_card(card, category, atmos_val, status_val, hilton_val):
    atmos_pts = get_rate(card.atmos_points, category)
    status_pts = get_rate(card.status_points, category)
    hilton_pts = get_rate(card.hilton_points, category)
    cashback_rate = get_rate(card.cashback, category)

    atmos_value = atmos_pts * atmos_val
    status_value = status_pts * status_val
    hilton_value = hilton_pts * hilton_val
    cash_value = cashback_rate

    total = atmos_value + status_value + hilton_value + cash_value
    return total, atmos_value, status_value, hilton_value, cash_value

def optimize_category(category, atmos_val=0.012, status_val=3000/135000, hilton_val=0.004):
    results = []
    for card in cards:
        total, a, s, h, c = value_for_card(card, category, atmos_val, status_val, hilton_val)
        results.append((card.name, total, a, s, h, c))
    results.sort(key=lambda x: x[1], reverse=True)
    return results

def main():
    if len(sys.argv) < 2:
        print("Usage: python optimizer.py <category> [atmos_val] [status_val] [hilton_val]")
        sys.exit(1)

    category = sys.argv[1]
    atmos_val = float(sys.argv[2]) if len(sys.argv) > 2 else 0.012
    status_val = float(sys.argv[3]) if len(sys.argv) > 3 else (3000/135000)
    hilton_val = float(sys.argv[4]) if len(sys.argv) > 4 else 0.004

    results = optimize_category(category, atmos_val, status_val, hilton_val)

    print(f"Category: {category}")
    print(f"{'Card':25s} {'Total%':>8s} {'Atmos%':>8s} {'Status%':>8s} {'Hilton%':>8s} {'Cash%':>8s}")
    for name, total, a, s, h, c in results:
        print(f"{name:25s} {total*100:8.4f} {a*100:8.4f} {s*100:8.4f} {h*100:8.4f} {c*100:8.4f}")

if __name__ == "__main__":
    main()
```

---

# optimizer.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Credit Card Spend Optimizer</title>
  <style>
    body { font-family: system-ui, sans-serif; margin: 20px; }
    label { display: block; margin-top: 10px; }
    input, select { padding: 4px; margin-top: 4px; }
    button { margin-top: 12px; padding: 6px 10px; }
    table { border-collapse: collapse; margin-top: 20px; width: 100%; max-width: 900px; }
    th, td { border: 1px solid #ccc; padding: 6px 8px; text-align: left; }
    th { background: #f5f5f5; }
  </style>
</head>
<body>
  <h1>Credit Card Spend Optimizer</h1>

  <h2>Valuations</h2>
  <label>Atmos redeemable point value:
    <input type="number" id="atmos_value" step="0.0001" value="0.012">
  </label>
  <label>Status point value:
    <input type="number" id="status_value" step="0.0001" value="0.022222">
  </label>
  <label>Hilton point value:
    <input type="number" id="hilton_value" step="0.0001" value="0.004">
  </label>

  <h2>Category</h2>
  <label>Choose category:
    <select id="category">
      <option value="groceries">Groceries</option>
      <option value="gas">Gas (non-Costco)</option>
      <option value="gas_costco">Gas at Costco</option>
      <option value="dining">Dining</option>
      <option value="online_retail">Online retail</option>
      <option value="travel_general">Travel (general)</option>
      <option value="alaska_airlines">Alaska Airlines</option>
      <option value="hawaiian_airlines">Hawaiian Airlines</option>
      <option value="foreign">Foreign purchases</option>
      <option value="hilton_stays">Hilton stays</option>
      <option value="disney_streaming">Disney streaming</option>
      <option value="costco_general">Costco general</option>
      <option value="other">Other</option>
    </select>
  </label>

  <button id="run">Run Optimizer</button>

  <h2>Results</h2>
  <table id="results">
    <thead>
      <tr>
        <th>Card</th>
        <th>Total Value (%)</th>
        <th>Atmos (%)</th>
        <th>Status (%)</th>
        <th>Hilton (%)</th>
        <th>Cash (%)</th>
      </tr>
    </thead>
    <tbody></tbody>
  </table>

  <script>
    const cards = [
      {
        name: "Atmos Summit",
        atmos: { alaska_airlines: 3, dining: 3, foreign: 3, other: 1 },
        status: { other: 0.5 },
        hilton: {},
        cashback: {}
      },
      {
        name: "Atmos Ascent",
        atmos: {
          alaska_airlines: 3,
          hawaiian_airlines: 3,
          ev_charging: 2,
          gas: 2,
          transit: 2,
          internet_cable: 2,
          streaming: 2,
          other: 1
        },
        status: { other: 0.3333333333 },
        hilton: {},
        cashback: {}
      },
      {
        name: "Hawaiian MC (Atmos)",
        atmos: {
          hawaiian_airlines: 3,
          gas: 2,
          dining: 2,
          groceries: 2,
          other: 1
        },
        status: { other: 0.3333333333 },
        hilton: {},
        cashback: {}
      },
      {
        name: "Amex Blue Cash Everyday",
        atmos: {},
        status: {},
        hilton: {},
        cashback: {
          groceries: 0.03,
          online_retail: 0.03,
          gas: 0.03,
          other: 0.01
        }
      },
      {
        name: "Amex Hilton Aspire",
        atmos: {},
        status: {},
        hilton: {
          hilton_stays: 14,
          flights: 7,
          car_rentals: 7,
          dining: 7,
          other: 3
        },
        cashback: {}
      },
      {
        name: "Disney Premier Visa",
        atmos: {},
        status: {},
        hilton: {},
        cashback: {
          disney_streaming: 0.05,
          gas: 0.02,
          groceries: 0.02,
          dining: 0.02,
          disney_us: 0.02,
          other: 0.01
        }
      },
      {
        name: "Costco Anywhere Visa",
        atmos: {},
        status: {},
        hilton: {},
        cashback: {
          gas_costco: 0.05,
          gas: 0.04,
          dining: 0.03,
          travel_general: 0.03,
          costco_general: 0.02,
          other: 0.01
        }
      }
    ];

    function getRate(map, category) {
      if (category in map) return map[category];
      if ("other" in map) return map["other"];
      return 0;
    }

    document.getElementById("run").addEventListener("click", () => {
      const atmosVal = parseFloat(document.getElementById("atmos_value").value) || 0;
      const statusVal = parseFloat(document.getElementById("status_value").value) || 0;
      const hiltonVal = parseFloat(document.getElementById("hilton_value").value) || 0;
      const category = document.getElementById("category").value;

      const rows = [];

      for (const card of cards) {
        const atmosPts = getRate(card.atmos, category);
        const statusPts = getRate(card.status, category);
        const hiltonPts = getRate(card.hilton, category);
        const cashbackRate = getRate(card.cashback, category);

        const atmosValue = atmosPts * atmosVal;
        const statusValue = statusPts * statusVal;
        const hiltonValue = hiltonPts * hiltonVal;
        const cashValue = cashbackRate;

        const total = atmosValue + statusValue + hiltonValue + cashValue;

        rows.push({
          name: card.name,
          total,
          atmosValue,
          statusValue,
          hiltonValue,
          cashValue
        });
      }

      rows.sort((a, b) => b.total - a.total);

      const tbody = document.querySelector("#results tbody");
      tbody.innerHTML = "";
      for (const r of rows) {
        const tr = document.createElement("tr");
        tr.innerHTML = `
          <td>${r.name}</td>
          <td>${(r.total * 100).toFixed(4)}</td>
          <td>${(r.atmosValue * 100).toFixed(4)}</td>
          <td>${(r.statusValue * 100).toFixed(4)}</td>
          <td>${(r.hiltonValue * 100).toFixed(4)}</td>
          <td>${(r.cashValue * 100).toFixed(4)}</td>
        `;
        tbody.appendChild(tr);
      }
    });
  </script>
</body>
</html>
```

---

# data.csv
```csv
card_name,category,atmos_points_per_dollar,status_points_per_dollar,hilton_points_per_dollar,cashback_rate
Atmos Summit,alaska_airlines,3,0.5,0,0
Atmos Summit,dining,3,0.5,0,0
Atmos Summit,foreign,3,0.5,0,0
Atmos Summit,other,1,0.5,0,0
Atmos Ascent,alaska_airlines,3,0.3333333333,0,0
Atmos Ascent,hawaiian_airlines,3,0.3333333333,0,0
Atmos Ascent,ev_charging,2,0.3333333333,0,0
Atmos Ascent,gas,2,0.3333333333,0,0
Atmos Ascent,transit,2,0.3333333333,0,0
Atmos Ascent,internet_cable,2,0.3333333333,0,0
Atmos Ascent,streaming,2,0.3333333333,0,0
Atmos Ascent,other,1,0.3333333333,0,0
Hawaiian MC (Atmos),hawaiian_airlines,3,0.3333333333,0,0
Hawaiian MC (Atmos),gas,2,0.3333333333,0,0
Hawaiian MC (Atmos),dining,2,0.3333333333,0,0
Hawaiian MC (Atmos),groceries,2,0.3333333333,0,0
Hawaiian MC (Atmos),other,1,0.3333333333,0,0
Amex Blue Cash Everyday,groceries,0,0,0,0.03
Amex Blue Cash Everyday,online_retail,0,0,0,0.03
Amex Blue Cash Everyday,gas,0,0,0,0.03
Amex Blue Cash Everyday,other,0,0,0,0.01
Amex Hilton Aspire,hilton_stays,0,0,14,0
Amex Hilton Aspire,flights,0,0,7,0
Amex Hilton Aspire,car_rentals,0,0,7,0
Amex Hilton Aspire,dining,0,0,7,0
Amex Hilton Aspire,other,0,0,3,0
Disney Premier Visa,disney_streaming,0,0,0,0.05
Disney Premier Visa,gas,0,0,0,0.02
Disney Premier Visa,groceries,0,0,0,0.02
Disney Premier Visa,dining,0,0,0,0.02
Disney Premier Visa,disney_us,0,0,0,0.02
Disney Premier Visa,other,0,0,0,0.01
Costco Anywhere Visa,gas_costco,0,0,0,0.05
Costco Anywhere Visa,gas,0,0,0,0.04
Costco Anywhere Visa,dining,0,0,0,0.03
Costco Anywhere Visa,travel_general,0,0,0,0.03
Costco Anywhere Visa,costco_general,0,0,0,0.02
Costco Anywhere Visa,other,0,0,0,0.01
```

---

# model.md
```md
# Credit Card
