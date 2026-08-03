# 26. Personal Diary
# Store diary entries inside a text file.
# Menu
#     • Add entry
#     • View entries
#     • Search by date
#     • Exit
# Practice
#     • .txt files
#     • read()
#     • write()
#     • append()
#     • functions
# -------------------------------------
# diary.txt ///Python will automatically create diary.txt

def add_entry():
    date = input("Date (YYYY-MM-DD): ")
    entry = input("Write your diary entry: ")

    with open("diary.txt", "a") as file:
        file.write(f"{date} | {entry}\n")

        print("Entry saved successfully!")    

def view_entries():
    with open("diary.txt", "r") as file:
        content = file.read()
        
        if content:
            print(content)
        else:
            print("No diary entries found.")
        

def search_by_date():
    date = input("Enter date: ")

    with open("diary.txt", "r") as file:
        for line in file:
            if date in line:
                print(line)

while True:
    print("--- Personal Diary ---")
    print("\n1. Add Entry")
    print("2. View Entries")
    print("3. Search by Date")
    print("4. Exit")

    choice = int(input("Choose: "))

    if choice == 1:
       add_entry()

    elif choice == 2:
        view_entries()

    elif choice == 3:
        search_by_date()

    elif choice == 4:
        print("Goodbye!")
        break
    
    else:           
        print("Invalid choice.")

