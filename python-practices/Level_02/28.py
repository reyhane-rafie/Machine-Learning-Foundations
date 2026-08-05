# 28. Contact Book
# Store
#     • Name
#     • Phone
#     • Email
# Features
#     • Add
#     • Delete
#     • Search
#     • Save automatically
# Practice
#     • JSON
#     • dictionaries
#     • file handling
# ----------------------------------

import json


def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)
    print("Contact added successfully!")


def delete_contact(contacts):
    name = input("Name to delete: ")

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def search_contact(contacts):
    name = input("Search name: ")

    if name in contacts:
        print("\nContact Found")
        print("Name :", name)
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
    else:
        print("Contact not found.")


def show_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return

    print("\n--- Contacts ---")

    for name, info in contacts.items():
        print(f"Name : {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print("-" * 25)


# Load contacts once when the program starts
contacts = load_contacts()


while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Show All Contacts")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_contact(contacts)

    elif choice == "2":
        delete_contact(contacts)

    elif choice == "3":
        search_contact(contacts)

    elif choice == "4":
        show_contacts(contacts)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")       