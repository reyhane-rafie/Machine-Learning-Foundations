# 27. Study Tracker (Persistent Version)
# Upgrade Project 25.
# Store study sessions in a CSV file.
# Each row:
# Date
# Subject
# Hours
# Show
#     • Total hours
#     • Hours by subject
#     • Weekly total
# Practice
#     • CSV
#     • file handling
#     • dictionaries
# -----------------------------------------

import csv


def add_session():

    date = input("Date: ")
    subject = input("Subject: ")
    hours = float(input("Hours: "))

    with open("study_sessions.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([date, subject, hours])

    print("Session added!")


def read_sessions():

    with open("study_sessions.csv", "r") as file:

        reader = csv.reader(file)

        for row in reader:
            print(row)



def total_hours():

    total = 0

    with open("study_sessions.csv", "r") as file:

        reader = csv.reader(file)

        for row in reader:
            total += float(row[2])

    return total



def hours_by_subject():

    subject_hours = {}

    with open("study_sessions.csv", "r") as file:

        reader = csv.reader(file)

        for row in reader:

            subject = row[1]
            hours = float(row[2])

            if subject in subject_hours:
                subject_hours[subject] += hours

            else:
                subject_hours[subject] = hours

    return subject_hours



def weekly_total():

    start_date = input("Enter week start date: ")

    total = 0

    with open("study_sessions.csv", "r") as file:

        reader = csv.reader(file)

        for row in reader:

            date = row[0]
            hours = float(row[2])

            if date >= start_date:
                total += hours

    return total



while True:

    print("\n--- Study Tracker ---")
    print("1. Add Study Session")
    print("2. Show Sessions")
    print("3. Total Hours")
    print("4. Hours By Subject")
    print("5. Weekly Total")
    print("6. Exit")

    choice = input("Choose: ")


    if choice == "1":

        add_session()


    elif choice == "2":

        read_sessions()


    elif choice == "3":

        print("Total Hours:", total_hours())


    elif choice == "4":

        print(hours_by_subject())


    elif choice == "5":

        print("Weekly Total:", weekly_total())


    elif choice == "6":

        print("Goodbye!")
        break


    else:

        print("Invalid choice")
