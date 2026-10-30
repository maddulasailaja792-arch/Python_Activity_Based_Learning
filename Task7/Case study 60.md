# Problem Statement
The Manufacturing Quality Control Matrix analyses production quantities and defective units across different products and batches. The program calculates the defect percentage for each batch and compares it with a predefined quality threshold. If the defect percentage exceeds the threshold, the batch is identified as Rejected / Quality Check Required. Otherwise, the batch is marked as Accepted. This helps manufacturers maintain product quality and identify batches that require improvement.
# Algorithm
1. Start the program.
2. Define the maximum acceptable defect percentage as 5%.
3. Enter the number of products or batches to analyse.
4. For each batch, enter:
   - Product name
   - Batch number
   - Total production quantity
   - Number of defective units
5. Calculate the defect percentage using the formula:
   Defect Percentage = (Defective Units / Total Production Quantity) × 100
6. Compare the defect percentage with the 5% quality threshold.
7. If the defect percentage is greater than 5%, mark the batch as Rejected.
8. Otherwise, mark the batch as Accepted.
9. Display the product name, batch number, production quantity, defective units, defect percentage, and quality status.
10. Stop the program.
# Mermaid Flowchart
``` mermaid
flowchart TD
    A([Start]) --> B[Set Quality Threshold = 5%]
    B --> C[Enter Number of Batches]
    C --> D[Enter Product Name and Batch Number]
    D --> E[Enter Production Quantity]
    E --> F[Enter Defective Units]
    F --> G[Calculate Defect Percentage]
    G --> H{Defect Percentage > 5%?}
    H -- Yes --> I[Mark Batch as Rejected]
    H -- No --> J[Mark Batch as Accepted]
    I --> K[Display Batch Details and Status]
    J --> K
```
# Sample Input
Enter the number of batches: 3

Batch 1
Enter product name: Steel Rod
Enter batch number: B101
Enter total production quantity: 1000
Enter defective units: 20

Batch 2
Enter product name: Plastic Bottle
Enter batch number: B102
Enter total production quantity: 500
Enter defective units: 40

Batch 3
Enter product name: Metal Sheet
Enter batch number: B103
Enter total production quantity: 800
Enter defective units: 16
    K --> L{More Batches?}
    L -- Yes --> D
    L -- No --> M([Stop])
