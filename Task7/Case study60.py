```python
# Manufacturing Quality Control Matrix

threshold = 5.0

n = int(input("Enter the number of batches: "))

print("\n--- Manufacturing Quality Control Report ---")

for i in range(1, n + 1):
    print(f"\nBatch {i}")

    product = input("Enter product name: ")
    batch_no = input("Enter batch number: ")
    production = int(input("Enter total production quantity: "))
    defective = int(input("Enter defective units: "))

    if production <= 0:
        print("Invalid production quantity!")
        continue

    if defective < 0 or defective > production:
        print("Invalid number of defective units!")
        continue

    defect_percentage = (defective / production) * 100

    if defect_percentage > threshold:
        status = "Rejected - Quality Check Required"
    else:
        status = "Accepted"

    print("\nProduct Name:", product)
    print("Batch Number:", batch_no)
    print("Production Quantity:", production)
    print("Defective Units:", defective)
    print("Defect Percentage:", round(defect_percentage, 2), "%")
    print("Quality Status:", status)

print("\nQuality Control Analysis Completed.")
```
