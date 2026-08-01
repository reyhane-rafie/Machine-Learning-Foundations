# 24. University GPA Calculator
# Input:
# Course name
# Credits
# Grade

# Calculate GPA.
# ==============================

courses = []


def add_course(courses):

    name = input("Course name: ")
    credits = int(input("Credits: "))
    grade = float(input("Grade: "))

    courses.append({
        "name": name,
        "credits": credits,
        "grade": grade
    })

    print("Course added!")


def calculate_gpa(courses):

    total_points = 0
    total_credits = 0

    for course in courses:

        total_points += course["grade"] * course["credits"]

        total_credits += course["credits"]

    if total_credits > 0:
        return total_points / total_credits

    else:
        return 0


def show_courses(courses):

    for course in courses:
        print(
            course["name"],
            "- Grade:",
            course["grade"],
            "- Credits:",
            course["credits"]
        )


while True:

    print("\n--- GPA Calculator ---")
    print("1. Add Course")
    print("2. Show Courses")
    print("3. Calculate GPA")
    print("4. Exit")

    choice = int(input("Choose: "))


    if choice == 1:

        add_course(courses)


    elif choice == 2:

        show_courses(courses)


    elif choice == 3:

        print("GPA:", calculate_gpa(courses))


    elif choice == 4:

        print("Goodbye!")
        break


    else:

        print("Invalid choice")