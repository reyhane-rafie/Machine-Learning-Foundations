# 22. Bank Management System
# Multiple users:
# Deposit
# Withdraw
# Transfer
# Check Balance
# =====================

accounts = {
    "Ali": 1000,
    "Sara": 1500,
    "John": 800
}


def deposit(accounts, user):
    amount = float(input("Deposit amount: "))

    accounts[user] += amount

    print("Deposit successful!")
    print("New balance:", accounts[user])


def withdraw(accounts, user):
    amount = float(input("Withdraw amount: "))

    if amount <= accounts[user]:
        accounts[user] -= amount

        print("Withdrawal successful!")
        print("New balance:", accounts[user])

    else:
        print("Insufficient balance")


def transfer(accounts, sender):

    receiver = input("Receiver Name: ")

    if receiver not in accounts:
        print("Receiver does not exist")
        return

    amount = float(input("Transfer amount: "))

    if amount <= accounts[sender]:
        accounts[sender] -= amount
        accounts[receiver] += amount

        print("Transfer successful!")

    else:
        print("Insufficient balance")


def check_balance(accounts, user):
    print("Current balance:", accounts[user])


while True:

    print("\n--- Bank Management System ---")

    print("Users:")
    for user in accounts:
        print("-", user)

    user = input("\nEnter your username: ")

    if user not in accounts:
        print("User does not exist")
        continue


    while True:

        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check Balance")
        print("5. Logout")

        choice = input("Choose an option: ")


        if choice == "1":
            deposit(accounts, user)

        elif choice == "2":
            withdraw(accounts, user)

        elif choice == "3":
            transfer(accounts, user)

        elif choice == "4":
            check_balance(accounts, user)

        elif choice == "5":
            print("Logged out.")
            break

        else:
            print("Invalid choice")