# 36. Student Grade Analysis
# Read a CSV.
# Calculate
#     • Average
#     • Highest score
#     • Lowest score
#     • Top students
# Practice
#     • DataFrame
#     • filtering
# ----------------------------

import pandas as pd 

students = pd.read_csv("students.csv")

print(students)

students["Score"]

average = students["Score"].mean()

print("Average Score:", round(average, 2))

highest = students["Score"].max()

lowest = students["Score"].min()

print("Highest Score:", highest)
print("Lowest Score:", lowest)

top_students = students[students["Score"] >= 90]

print("\n--- Top Students ---")
print(top_students)



