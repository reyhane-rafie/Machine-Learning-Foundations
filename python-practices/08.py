# 8. Student Management System
# Store
# Student name
# Score

# Menu
# Add student

# Show students

# Highest score

# Average

# Exit
# ########
# Use lists.
# ---------------------
students = [
    ["Ali", 85],
    ["Sara", 92],
    ["John", 78]
]

def add_student():
    name = input("Enter student name: ")
    score = int(input("Enter score: "))
   
    students.append([name, score])

def show_students():
    for student in students:
        print(student[0], student[1])

def highest_score():
    scores = []
   
    for student in students:
        scores.append(student[1])
    return max(scores)    

def average_score():
    scores = []
   
    for student in students:
        scores.append(student[1])
    return sum(scores) / len(scores)

while True:
    print(
        "\n1. Add student"
        "\n2. Show students"
        "\n3. Highest score"
        "\n4. Average"
        "\n5. Exit"
)

    choice = int(input("choose : "))

    if choice == 1:
        add_student()

    elif choice == 2:
        show_students()

    elif choice == 3:
        print("Highest score:", highest_score())

    elif choice == 4:
        print("Average:", average_score())

    elif choice == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid choice")