# 13. Expense Tracker

# User enters:
# Food
# Transport
# Books
# Rent

# Calculate:
# Total spending
# Largest expense
# ---------------------

expenses = {
    "Food": 0,
    "Transport": 0,
    "Books": 0,
    "Rent": 0
}


def add_expense():
    category = input("Choose a category (Food, Transport, Books, Rent): ")
    amount = float(input("Enter expense amount: "))

    if category in expenses:
        expenses[category] += amount
    else:
        print("Invalid category!")


def show_expenses():
    for category, amount in expenses.items():
        print(category, ":", amount)


def total_spending():
    return sum(expenses.values())


def largest_expense():
    largest = max(expenses.values())

    for category, amount in expenses.items():
        if amount == largest:
            return category, amount


while True:

    print("\nMenu")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Spending")
    print("4. Largest Expense")
    print("5. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        add_expense()

    elif choice == 2:
        show_expenses()

    elif choice == 3:
        print("Total Spending:", total_spending())

    elif choice == 4:
        category, amount = largest_expense()
        print("Largest Expense:", category, "-", amount)

    elif choice == 5:
        print("Done!")
        break

    else:
        print("Invalid choice")

print("Have a good day!")                 

               
