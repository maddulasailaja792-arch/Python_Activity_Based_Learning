# Problem Statement
The ATM Menu-Driven Banking Simulation is a Python program designed to perform basic banking operations through a repeated menu. The user can check their account balance, deposit money, withdraw money, and view a transaction summary. The program validates user inputs, prevents invalid transactions, and enforces account limits, such as minimum withdrawal amounts, maximum withdrawal limits, and insufficient balance checks. The menu continues to appear until the user selects the Exit option.
# Algorithm
1. Start the program.
2. Initialize the account balance, transaction count, total deposits, and total withdrawals.
# Display the ATM menu:
   -
     1. Balance Inquiry
   -
     2. Deposit Money
   -
     3. Withdraw Money
   -
     4. Transaction Summary
   -
     5. Exit
4. Read the user's menu choice.
5. If the choice is 1, display the current account balance.
6. If the choice is 2:
   - Enter the deposit amount.
   - Validate the amount.
   - If valid, update the balance and total deposits.
7. If the choice is 3:
   - Enter the withdrawal amount.
   - Check the withdrawal limit and available balance.
   - If valid, deduct the amount and update total withdrawals.
8. If the choice is 4, display the transaction summary, including total deposits, total withdrawals, and the current balance.
9. If the choice is 5, display a thank-you message and terminate the program.
10. If the choice is invalid, display an error message.
11. Repeat the menu until the user selects Exit.
12. Stop the program.
3. Mermaid Flowchart
``` mermaid
flowchart TD
    A([Start]) --> B[Initialize balance and transaction totals]
    B --> C[Display ATM Menu]
    C --> D[/Enter choice/]
    D --> E{Check choice}

    E -->|1| F[Display account balance]
    F --> C

    E -->|2| G[/Enter deposit amount/]
    G --> H{Amount greater than zero?}
    H -->|Yes| I[Update balance and total deposits]
    H -->|No| J[Display invalid amount]
    I --> C
    J --> C

    E -->|3| K[/Enter withdrawal amount/]
    K --> L{Amount within withdrawal limit?}
    L -->|No| M[Display limit error]
    L -->|Yes| N{Sufficient balance?}
    N -->|No| O[Display insufficient balance]
    N -->|Yes| P[Deduct amount and update totals]
    M --> C
    O --> C
    P --> C

    E -->|4| Q[Display transaction summary]
    Q --> C

    E -->|5| R[Display thank-you message]
    R --> S([Stop])

    E -->|Invalid| T[Display invalid choice]
    T --> C
```
# Sample Input
===== ATM MENU =====
1. Balance Inquiry
2. Deposit Money
3. Withdraw Money
4. Transaction Summary
5. Exit

Enter your choice: 1
Output:
Available Balance: Rs. 5000.00
  



































Think
