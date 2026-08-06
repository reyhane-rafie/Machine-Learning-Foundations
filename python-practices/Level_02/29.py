# 29. Expense Tracker (Persistent)
# Upgrade previous expense tracker.
# Save every expense to a CSV.
# Show
#     • Monthly total
#     • Largest expense
#     • Category totals
# Practice
#     • CSV
#     • loops
#     • file reading
# ----------------------------------------

import csv


def add_expense():
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category (Food/Transport/Books/Rent): ")
    amount = float(input("Amount: "))

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([date, category, amount])

def show_expenses():
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

def monthly_total():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0].startswith(month):
                total += float(row[2])

    return total


def largest_expense():
    largest = 0
    largest_row = None

    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            amount = float(row[2])

            if amount > largest:
                largest = amount
                largest_row = row

    return largest_row


def category_totals():
    totals = {}

    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            category = row[1]
            amount = float(row[2])

            if category in totals:
                totals[category] += amount
            else:
                totals[category] = amount

    return totals

while True:

    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Monthly Total")
    print("4. Largest Expense")
    print("5. Category Totals")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        total = monthly_total()
        print("Monthly Total:", total)

    elif choice == "4":
        expense = largest_expense()

        if expense:
            print("Largest Expense:")
            print("Date:", expense[0])
            print("Category:", expense[1])
            print("Amount:", expense[2])
        else:
            print("No expenses found.")

    elif choice == "5":
        totals = category_totals()

        print("\nCategory Totals:")

        for category, amount in totals.items():
            print(category, ":", amount)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")