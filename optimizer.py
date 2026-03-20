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
    if "general" in mapping:
        return mapping["general"]
    return 0.0

cards: List[Card] = [
    Card(
        name="Atmos Summit",
        atmos_points={"alaska_airlines": 3, "hawaiian_airlines": 3, "dining": 3, "foreign": 3, "general": 1},
        status_points={"general": 0.5},
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
            "general": 1,
        },
        status_points={"general": 0.3333333333},
        hilton_points={},
        cashback={},
    ),
    Card(
        name="Hawaiian MC (Atmos)",
        atmos_points={
            "alaska_airlines": 3,
            "hawaiian_airlines": 3,
            "gas": 2,
            "dining": 2,
            "groceries": 2,
            "general": 1,
        },
        status_points={"general": 0.3333333333},
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
            "general": 0.01,
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
            "general": 3,
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
            "general": 0.01,
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
    print(f"{'Card':25s} {'Total':>10s} {'Atmos':>8s} {'Status':>8s} {'Hilton':>8s} {'Cash':>8s}")
    for name, total, a, s, h, c in results:
        print(f"{name:25s} {total*100:9.1f}% {a*100:7.2f}¢ {s*100:7.2f}¢ {h*100:7.2f}¢ {c*100:7.2f}¢")

if __name__ == "__main__":
    main()
