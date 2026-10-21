import pandas as pd
import matplotlib.pyplot as plt

daily_data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"],
    "Study_Hours": [2, 3, 1.5, 4, 2.5, 5, 3]    
}

subject_data = {
    "Subject": ["Python", "Machine Learning", "GIS", "Remote Sensing"],
    "Hours": [6, 5, 4, 6]
}

daily_df = pd.DataFrame(daily_data)
subject_df = pd.DataFrame(subject_data)

# Chart 1: Daily study hours
plt.figure()
plt.bar(daily_df["Day"], daily_df["Study_Hours"])
plt.title("Study Time Dashboard")
plt.xlabel("Day")
plt.ylabel("Hours")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Chart 2: Study time distribution by subject
plt.figure()
plt.pie(
    subject_df["Hours"],
    labels=subject_df["Subject"],
    autopct="%1.1f%%"
)
plt.title("Study Time Distribution by Subject")
plt.show()
