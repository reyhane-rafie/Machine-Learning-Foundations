# 9. Restaurant Ordering System
# Menu
# Pizza

# Burger

# Coffee

# Tea
# User orders several items.
# Calculate total bill.
# Bonus
# Apply
# 10% discount

# if total > 50
# ---------------

menu = {
    "pizza": 12,
    "burger": 8,
    "coffee": 3,
    "tea": 2
}

total = 0

def show_menu():
    print(
        "\nPizza - $12"
        "\nBurger - $8"
        "\nCoffee - $3"
        "\nTea - $2"
    )

while True:
    show_menu()

    order = input("\nWhat do you have in mind?(type done to finish) :") 

    if order == "done":
        break

    if order in menu:
        total = total + menu[order]
        print("Added:", order)

    else:
        print("Item not available")    


if total > 50:
        discount = total * 0.10
        total = total - discount
        print("10% discount applied!")  

print("Final bill:", total)