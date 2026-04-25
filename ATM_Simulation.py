# simple ATM simulation

# Database
balance = 1000
transactions = []

# display balance
def show_balance():
    print("Your balance is:", balance)

# deposit money
def deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        transactions.append("Deposited " + str(amount))
        print("Amount deposited.")
    else:
        print("Invalid amount.")

# withdraw money
def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance and amount > 0:
        balance -= amount
        transactions.append("Withdrawn " + str(amount))
        print("Amount withdrawn.")
    else:
        print("Insufficient balance or invalid amount.")

# show statement
def statement():
    if len(transactions) == 0:
        print("No transactions found.")
    else:
        print("Transaction history:")
        for t in transactions:
            print(t)

# ATM menu
def atm():
    while True:
        print("Menu")
        print("1. Display Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Statement")
        print("5. Exit")
        print("-"*30)

        choice = int(input("Enter your choice: "))
        print("-"*30)

        if choice == 1:
            show_balance()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            statement()
        elif choice == 5:
            print("Thank you")
            break
        else:
            print("Invalid choice")

atm()