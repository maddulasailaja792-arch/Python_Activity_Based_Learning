# Problem Statement
Food Supply Chain Stock Reconciliation is a system used to manage and monitor food stock across several locations. It compares the quantities of food received, distributed, damaged, and remaining at each location. The system identifies stock discrepancies by comparing the expected remaining quantity with the actual remaining quantity. It also calculates the replenishment quantity required to maintain sufficient stock and avoid food shortages.
#  Algorithm
Step 1: Start the program.

Step 2: Enter the number of locations.

Step 3: For each location, enter:
- Location name
- Quantity of food received
- Quantity of food distributed
- Quantity of food damaged
- Actual remaining stock
- Minimum stock required
Step 4: Calculate the expected remaining stock using the formula:

Expected Stock = Received − Distributed − Damaged

Step 5: Calculate the stock discrepancy:

Discrepancy = Actual Remaining Stock − Expected Stock

Step 6: If the discrepancy is zero, display "Stock Matched"; otherwise, display "Stock Discrepancy Found."

Step 7: Calculate the replenishment requirement:

Replenishment = Maximum (0, Minimum Stock Required − Actual Remaining Stock)

Step 8: Display the expected stock, actual stock, discrepancy, and replenishment quantity for each location.

Step 9: Stop the program.
# Mermaid Flowchart
```mermaid
flowchart TD
    A([Start]) --> B[/Enter number of locations/]
    B --> C[/Enter location name and stock details/]
    C --> D[Calculate expected stock]
    D --> E[Received - Distributed - Damaged]
    E --> F[Calculate discrepancy]
    F --> G[Actual Stock - Expected Stock]
    G --> H{Is discrepancy zero?}
    H -- Yes --> I[Display Stock Matched]
    H -- No --> J[Display Stock Discrepancy]
    I --> K[Calculate replenishment]
    J --> K
    K --> L[Minimum Stock - Actual Stock]
    L --> M{Is replenishment positive?}
    M -- Yes --> N[Display replenishment quantity]
    M -- No --> O[Replenishment = 0]
    N --> P{More locations?}
    O --> P
    P -- Yes --> C
    P -- No --> Q([Stop])
```
# Sample Input
Enter number of locations: 2

Location 1
Enter location name: Warehouse
Enter quantity received: 1000
Enter quantity distributed: 600
Enter quantity damaged: 50
Enter actual remaining stock: 350
Enter minimum stock required: 500

Location 2
Enter location name: Canteen
Enter quantity received: 500
Enter quantity distributed: 300
Enter quantity damaged: 20
Enter actual remaining stock: 180
Enter minimum stock required: 250
