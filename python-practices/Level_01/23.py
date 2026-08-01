# 23. Hotel Booking System
# Rooms:
# Available
# Booked
# Cancel booking
# =======================

rooms = {
    101: "Available",
    102: "Available",
    103: "Available",
    104: "Available",
    105: "Available"
}


def show_available_rooms(rooms):

    print("\nAvailable Rooms:")

    for room, status in rooms.items():

        if status == "Available":
            print(room)


def book_room(rooms):

    room = int(input("Enter room number: "))

    if room in rooms:

        if rooms[room] == "Available":

            rooms[room] = "Booked"
            print("Room booked successfully!")

        else:
            print("The room is already taken")

    else:
        print("Room does not exist")


def cancel_booking(rooms):

    room = int(input("Enter room number: "))

    if room in rooms:

        if rooms[room] == "Booked":

            rooms[room] = "Available"
            print("Booking cancelled!")

        else:
            print("Room is already available")

    else:
        print("Room does not exist")


while True:

    print("\n--- Hotel Booking System ---")
    print("1. Show Available Rooms")
    print("2. Book Room")
    print("3. Cancel Booking")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        show_available_rooms(rooms)

    elif choice == "2":

        book_room(rooms)

    elif choice == "3":

        cancel_booking(rooms)

    elif choice == "4":

        print("Goodbye!")
        break

    else:

        print("Invalid choice")