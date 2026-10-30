# Inventory Matrix Reconciliation

products = ["Laptop", "Mobile", "Tablet"]

warehouses = ["Warehouse A", "Warehouse B", "Warehouse C"]

# Current stock in each warehouse
stock = [
    [50, 20, 30],
    [15, 40, 25],
    [35, 10, 20]
]

# Target stock in each warehouse
target = [
    [30, 30, 25],
    [25, 30, 25],
    [30, 20, 25]
]

surplus = []
shortage = []

# Identify surplus and shortage
for i in range(len(warehouses)):
    for j in range(len(products)):
        difference = stock[i][j] - target[i][j]

        if difference > 0:
            surplus.append([i, j, difference])
        elif difference < 0:
            shortage.append([i, j, -difference])

# Display inventory matrix
print("CURRENT INVENTORY")
for i in range(len(warehouses)):
    print(warehouses[i], stock[i])

print("\nSURPLUS STOCK")
for i, j, qty in surplus:
    print(products[j], "-", warehouses[i], ":", qty)

print("\nSHORTAGE STOCK")
for i, j, qty in shortage:
    print(products[j], "-", warehouses[i], ":", qty)

# Transfer products between warehouses
print("\nREQUIRED TRANSFERS")

for s in surplus:
    source, product, available = s

    for sh in shortage:
        destination, product2, required = sh

        if product == product2 and available > 0 and required > 0:
            transfer = min(available, required)

            stock[source][product] -= transfer
            stock[destination][product] += transfer

            available -= transfer
            sh[2] -= transfer

            print(
                products[product],
                ":",
                warehouses[source],
                "->",
                warehouses[destination],
                "=",
                transfer,
                "units"
            )

print("\nFINAL INVENTORY")
for i in range(len(warehouses)):
    print(warehouses[i], stock[i])

print("\nREMAINING SHORTAGES")
for i, j, qty in shortage:
    if qty > 0:
        print(products[j], "-", warehouses[i], ":", qty)
