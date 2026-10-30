```python
# ATM Menu-Driven Banking Simulation

balance = 5000.0

total_deposits = 0.0
total_withdrawals = 0.0
transactions = 0

MIN_DEPOSIT = 100
MAX_DEPOSIT = 50000

MIN_WITHDRAWAL = 100
MAX_WITHDRAWAL = 10000
MIN_BALANCE = 500

while True:
    print("\n===== ATM MENU =====")
    print("1. Balance Inquiry")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Available Balance: Rs. {balance:.2f}")

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: Rs. "))

            if amount < MIN_DEPOSIT:
                print("Minimum deposit is Rs. 100.")

            elif amount > MAX_DEPOSIT:
                print("Maximum deposit is Rs. 50000.")

            else:
                balance += amount
                total_deposits += amount
                transactions += 1

                print("Deposit successful!")
                print(f"Updated Balance: Rs. {balance:.2f}")

        except ValueError:
            print("Invalid input! Enter a numeric amount.")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: Rs. "))

            if amount < MIN_WITHDRAWAL:
                print("Minimum withdrawal is Rs. 100.")

            elif amount > MAX_WITHDRAWAL:
                print("Maximum withdrawal per transaction is Rs. 10000.")

            elif balance - amount < MIN_BALANCE:
                print("Transaction failed!")
                print("Insufficient balance or minimum balance violation.")

            else:
                balance -= amount
                total_withdrawals += amount
                transactions += 1

                print("Please collect your cash.")
                print(f"Remaining Balance: Rs. {balance:.2f}")

        except ValueError:
            print("Invalid input! Enter a numeric amount.")

    elif choice == "4":
        print("\n===== TRANSACTION SUMMARY =====")
        print(f"Total Deposits: Rs. {total_deposits:.2f}")
        print(f"Total Withdrawals: Rs. {total_withdrawals:.2f}")
        print(f"Number of Successful Transactions: {transactions}")
        print(f"Current Balance: Rs. {balance:.2f}")

    elif choice == "5":
        print("Thank you for using our ATM!")
        print(f"Final Balance: Rs. {balance:.2f}")
        break

    else:
        print("Invalid choice! Please select from 1 to 5.")
```
