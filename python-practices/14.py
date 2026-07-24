# 14. Library System
# Books:

# Borrow
# Return
# Show available books
# ---------------

books = [
    "Harry Potter",
    "The Hobbit",
    "1984",
    "Python Basics"
]


def borrow_book():
    book = input("Which book do you want to borrow? ")

    if book in books:
        books.remove(book)
        print("Book borrowed successfully.")
    else:
        print("The book is unavailable.")


def return_book():
    book = input("Which book do you want to return? ")

    if book not in books:
        books.append(book)
        print("Book returned successfully.")
    else:
        print("This book is already in the library.")


def show_books():
    print("\nAvailable Books:")

    for book in books:
        print("-", book)


while True:

    print("\n1. Borrow Book")
    print("2. Return Book")
    print("3. Show Available Books")
    print("4. Exit")

    choice = int(input("Choose one operation (1-4): "))

    if choice == 1:
        borrow_book()

    elif choice == 2:
        return_book()

    elif choice == 3:
        show_books()

    elif choice == 4:
        print("Done!")
        break

    else:
        print("Invalid choice.")

print("Have a great day!")              