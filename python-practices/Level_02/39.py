# 39. Study Habit Analyzer
# Analyze your own study log.
# Show
#     • Total hours
#     • Subject averages
#     • Most productive day
# Practice
#     • groupby()
#     • sorting
# ------------------------------

import pandas as pd

study = pd.read_csv("study_log.csv")


total_hours = study["Hours"].sum()


subject_averages = study.groupby("Subject")["Hours"].mean()

subject_averages = subject_averages.sort_values(ascending=False)

daily_hours = study.groupby("Date")["Hours"].sum()

daily_hours = daily_hours.sort_values(ascending=False)

most_productive_day = daily_hours.index[0]

most_productive_hours = daily_hours.iloc[0]

print("\n--- Study Habit Analysis ---")

print("Total hours:", total_hours)

print("\nSubject Averages:")
print(subject_averages)

print("\nMost Productive Day:")
print(most_productive_day, "-", most_productive_hours, "hours")