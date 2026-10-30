```python
# CASE STUDY 90: Integrated Campus Energy and Water Audit

# Cost rates
ELECTRICITY_RATE = 8       # Rs. per kWh
WATER_RATE = 2             # Rs. per litre

# Excess consumption thresholds (daily averages)
ELECTRICITY_LIMIT = 100    # kWh per day
WATER_LIMIT = 500          # litres per day

# Sample campus data
buildings = {
    "Library": {
        "electricity": [80, 90, 100],
        "water": [300, 320, 350]
    },
    "Laboratory": {
        "electricity": [120, 140, 160],
        "water": [400, 450, 500]
    },
    "Hostel": {
        "electricity": [150, 160, 180],
        "water": [600, 650, 700]
    }
}

results = []

print("INTEGRATED CAMPUS ENERGY AND WATER AUDIT")
print("-" * 60)

for name, data in buildings.items():

    electricity = data["electricity"]
    water = data["water"]

    # Calculate total consumption
    total_electricity = sum(electricity)
    total_water = sum(water)

    # Calculate costs
    electricity_cost = total_electricity * ELECTRICITY_RATE
    water_cost = total_water * WATER_RATE
    total_cost = electricity_cost + water_cost

    # Calculate percentage change
    if electricity[0] != 0:
        electricity_change = (
            (electricity[-1] - electricity[0])
            / electricity[0]
        ) * 100
    else:
        electricity_change = 0

    if water[0] != 0:
        water_change = (
            (water[-1] - water[0])
            / water[0]
        ) * 100
    else:
        water_change = 0

    # Identify excessive consumption
    avg_electricity = total_electricity / len(electricity)
    avg_water = total_water / len(water)

    alerts = []

    if avg_electricity > ELECTRICITY_LIMIT:
        alerts.append("Excess electricity")

    if avg_water > WATER_LIMIT:
        alerts.append("Excess water")

    if not alerts:
        alerts.append("Normal consumption")

    # Scoring method
    score = total_cost

    results.append({
        "name": name,
        "electricity": total_electricity,
        "water": total_water,
        "electricity_cost": electricity_cost,
        "water_cost": water_cost,
        "total_cost": total_cost,
        "electricity_change": electricity_change,
        "water_change": water_change,
        "alerts": ", ".join(alerts),
        "score": score
    })

# Display individual building reports
for item in results:
    print(f"\nBuilding: {item['name']}")
    print("Total electricity:", item["electricity"], "kWh")
    print("Total water:", item["water"], "litres")
    print("Electricity cost: Rs.", item["electricity_cost"])
    print("Water cost: Rs.", item["water_cost"])
    print("Total cost: Rs.", item["total_cost"])
    print("Electricity change: {:.2f}%".format(
        item["electricity_change"]))
    print("Water change: {:.2f}%".format(
        item["water_change"]))
    print("Consumption status:", item["alerts"])

# Rank buildings by total cost (highest first)
results.sort(key=lambda x: x["score"], reverse=True)

print("\nBUILDING RANKING")
print("-" * 40)

for rank, item in enumerate(results, start=1):
    print(
        f"{rank}. {item['name']} - "
        f"Score: Rs. {item['score']}"
    )

print("\nAudit completed successfully.")
```
