# 37. Weather Data Explorer
# Dataset

# Date
# Temperature
# Humidity
# Rainfall

# Answer
# - Hottest day
# - Rainiest day
# - Average rainfall

# Practice
# - Pandas
# -------------------------------

import pandas as pd


weather = pd.read_csv("weather.csv")

print(weather)


highest_temperature = weather["Temperature"].max()

hottest_day = weather[
    weather["Temperature"] == highest_temperature
]


highest_rainfall = weather["Rainfall"].max()

rainiest_day = weather[
    weather["Rainfall"] == highest_rainfall
]


average_rainfall = weather["Rainfall"].mean()


print("\n--- Weather Analysis ---")


print("\nHottest Day:")
print(hottest_day[["Date", "Temperature"]])


print("\nRainiest Day:")
print(rainiest_day[["Date", "Rainfall"]])


print("\nAverage Rainfall:")
print(round(average_rainfall, 2), "mm")