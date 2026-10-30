# Food Supply Chain Stock Reconciliation

locations = int(input("Enter number of locations: "))

for i in range(locations):
    print("\nLocation", i + 1)

    name = input("Enter location name: ")
    received = int(input("Enter quantity received: "))
    distributed = int(input("Enter quantity distributed: "))
    damaged = int(input("Enter quantity damaged: "))
    actual = int(input("Enter actual remaining stock: "))
    minimum = int(input("Enter minimum stock required: "))

    # Calculate expected remaining stock
    expected = received - distributed - damaged

    # Calculate stock discrepancy
    discrepancy = actual - expected

    # Calculate replenishment requirement
    replenishment = max(0, minimum - actual)

    # Display results
    print("\n--- Stock Reconciliation Report ---")
    print("Location:", name)
    print("Expected Remaining Stock:", expected)
    print("Actual Remaining Stock:", actual)
    print("Stock Discrepancy:", discrepancy)

    if discrepancy == 0:
        print("Status: Stock Matched")
    else:
        print("Status: Stock Discrepancy Found")

    print("Replenishment Required:", replenishment)
