# 6. ATM Simulator
# Menu
# 1 Deposit
# 2 Withdraw
# 3 Balance
# 4 Exit
# Balance changes after every operation.
# Practice
#     • while 
#     • functions 
#     • variables 
# ------------------------

balance = 0


def deposit(balance):
    amount = float(input("How much money do you want to deposit: "))
    balance = balance + amount
    return balance


def withdraw(balance):
    amount = float(input("How much money do you want to withdraw: "))

    if amount <= balance:
        balance = balance - amount
        return balance
    else:
        print("Not enough balance!")
        return balance


def show_balance(balance):
    print(f"Your balance is: {balance}")


while True:

    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Exit")

    choice = input("Choose an option (1,2,3,or4): ")

    if choice == "1":
        balance = deposit(balance)

    elif choice == "2":
        balance = withdraw(balance)

    elif choice == "3":
        show_balance(balance)

    elif choice == "4":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")      