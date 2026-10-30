# Energy Conservation Before-and-After Analysis

appliances = []

n = int(input("Enter the number of appliances: "))

for i in range(n):
    print("\nEnter details for appliance", i + 1)

    name = input("Appliance name: ")
    before = float(input("Electricity consumption before (kWh): "))
    after = float(input("Electricity consumption after (kWh): "))

    if before < 0 or after < 0:
        print("Consumption cannot be negative.")
        continue

    saved = before - after

    if before > 0:
        percentage = (saved / before) * 100
    else:
        percentage = 0

    appliances.append({
        "name": name,
        "before": before,
        "after": after,
        "saved": saved,
        "percentage": percentage
    })

# Rank appliances by energy saved
appliances.sort(key=lambda x: x["saved"], reverse=True)

# Display results
print("\n========== ENERGY CONSERVATION REPORT ==========")
print("{:<15} {:>10} {:>10} {:>10} {:>12} {:>6}".format(
    "Appliance", "Before", "After", "Saved", "Savings %", "Rank"
))

for rank, item in enumerate(appliances, start=1):
    print("{:<15} {:>10.2f} {:>10.2f} {:>10.2f} {:>11.2f}% {:>6}".format(
        item["name"],
        item["before"],
        item["after"],
        item["saved"],
        item["percentage"],
        rank
    ))

# Calculate total energy savings
total_before = sum(item["before"] for item in appliances)
total_after = sum(item["after"] for item in appliances)
total_saved = total_before - total_after

if total_before > 0:
    total_percentage = (total_saved / total_before) * 100
else:
    total_percentage = 0

print("\nTotal consumption before:", round(total_before, 2), "kWh")
print("Total consumption after:", round(total_after, 2), "kWh")
print("Total energy saved:", round(total_saved, 2), "kWh")
print("Overall savings percentage:", round(total_percentage, 2), "%")
