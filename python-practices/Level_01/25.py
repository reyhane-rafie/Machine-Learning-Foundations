# 25. Daily Study Tracker
# Input:
# Python
# TOEFL
# Research
# GIS

# Output:
# Hours studied
# Most studied subject
# Total hours
# ==================================

study = {
    "Python": 0,
    "TOEFL": 0,
    "Research": 0,
    "GIS": 0
}


def add_hours(study):
    subject = input("Subject: ")
    hours = float(input("Hours studied: "))

    if subject in study:
        study[subject] += hours
        print("Study hours added!")
    else:
        print("Subject not found.")


def show_hours(study):
    print("\nStudy Hours:")

    for subject, hours in study.items():
        print(subject, ":", hours)


def most_studied(study):
    subject = max(study, key=study.get)

    print("Most Studied Subject:")
    print(subject, "-", study[subject], "hours")


def total_hours(study):
    return sum(study.values())


while True:

    print("\n--- Daily Study Tracker ---")
    print("1. Add Study Hours")
    print("2. Show Study Hours")
    print("3. Most Studied Subject")
    print("4. Total Hours")
    print("5. Exit")

    choice = int(input("Choose: "))

    if choice == 1:
        add_hours(study)

    elif choice == 2:
        show_hours(study)

    elif choice == 3:
        most_studied(study)

    elif choice == 4:
        print("Total Hours:", total_hours(study))

    elif choice == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid choice")    