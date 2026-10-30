# Environmental Monitoring Data Analyzer

# Nested list containing air-quality readings
readings = [
    [35, 45, 55],
    [65, 80, 95],
    [110, 125, 40]
]

# Threshold values
good_limit = 50
moderate_limit = 100

# Convert nested list into a single list
all_readings = []

for location in readings:
    for value in location:
        all_readings.append(value)

# Calculate statistics
average = sum(all_readings) / len(all_readings)
maximum = max(all_readings)
minimum = min(all_readings)

# Display readings
print("Environmental Monitoring Data Analyzer")
print("---------------------------------------")
print("Readings:", readings)
print("Average Reading:", round(average, 2))
print("Maximum Reading:", maximum)
print("Minimum Reading:", minimum)

# Classify each observation
print("\nClassification of Observations:")

for i, location in enumerate(readings, start=1):
    for value in location:

        if value <= good_limit:
            category = "Good"
        elif value <= moderate_limit:
            category = "Moderate"
        else:
            category = "Poor"

        print("Location", i, "- Reading:", value,
              "- Category:", category)
