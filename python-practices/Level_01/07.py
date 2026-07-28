# 7. Simple Calculator
# Supports
# +
# -
# *
# /
# Runs until Exit.
# Use functions like
# add()

# subtract()

# multiply()

# divide()
# ---------------------
# Easy vesion
# def get_numbers():
#     number1 = float(input("Enter first number: "))
#     number2 = float(input("Enter second number: "))
#     return number1, number2
# --------------------

def get_numbers():
    while True:
        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            return number1, number2

        except ValueError:
            print("Please enter numbers only!")


def add():
    number1, number2 = get_numbers()
    return number1 + number2


def subtract():
    number1, number2 = get_numbers()
    return number1 - number2


def multiply():
    number1, number2 = get_numbers()
    return number1 * number2


def divide():
    number1, number2 = get_numbers()

    if number2 != 0:
        return number1 / number2
    else:
        return "Cannot divide by zero"


while True:

    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        print("Result:", add())

    elif choice == "2":
        print("Result:", subtract())

    elif choice == "3":
        print("Result:", multiply())

    elif choice == "4":
        print("Result:", divide())

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice")