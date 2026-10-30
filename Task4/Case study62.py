# Water Distribution Fairness Analysis

areas = {
    "Area A": {
        "demand": [1000, 1200, 1100],
        "supply": [900, 1000, 950]
    },
    "Area B": {
        "demand": [1200, 1300, 1250],
        "supply": [1000, 1100, 1000]
    },
    "Area C": {
        "demand": [800, 900, 850],
        "supply": [750, 850, 800]
    },
    "Area D": {
        "demand": [1500, 1600, 1550],
        "supply": [1000, 1050, 950]
    }
}

results = {}

print("WATER DISTRIBUTION FAIRNESS ANALYSIS")
print("-" * 75)

for area, data in areas.items():
    total_demand = sum(data["demand"])
    total_supply = sum(data["supply"])

    shortage = max(0, total_demand - total_supply)

    supply_percentage = (total_supply / total_demand) * 100

    shortage_percentage = (shortage / total_demand) * 100

    results[area] = {
        "demand": total_demand,
        "supply": total_supply,
        "shortage": shortage,
        "supply_percentage": supply_percentage,
        "shortage_percentage": shortage_percentage
    }

# Display area-wise results
print(f"{'Area':<10} {'Demand':>10} {'Supply':>10} "
      f"{'Shortage':>10} {'Supply %':>12}")

for area, data in results.items():
    print(f"{area:<10} {data['demand']:>10} "
          f"{data['supply']:>10} {data['shortage']:>10} "
          f"{data['supply_percentage']:>11.2f}%")

# Identify the most underserved area
most_underserved = max(
    results,
    key=lambda area: results[area]["shortage_percentage"]
)

print("\nMOST UNDERSERVED AREA:", most_underserved)

print("Shortage:",
      results[most_underserved]["shortage"], "litres")

print("Shortage Percentage:",
      f"{results[most_underserved]['shortage_percentage']:.2f}%")

# Compare distribution fairness
print("\nFAIRNESS ANALYSIS")

for area, data in results.items():
    print(f"{area}: {data['shortage_percentage']:.2f}% shortage")
