# 42. Weather Dashboard
# Plot
#     • Temperature
#     • Humidity
#     • Rainfall
# Practice
#     • line plots
#     • legends
# --------------------------

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"],
    
    "Temperature": [24, 26, 23, 21, 22, 25, 27],
    
    "Humidity": [55, 52, 65, 72, 68, 60, 50],
    
    "Rainfall": [0.0, 0.0, 4.5, 8.2, 3.1, 0.0, 0.0]    
}

df = pd.DataFrame(data)

plt.plot(df["Day"], df["Temperature"], label="Temperature")
plt.plot(df["Day"], df["Humidity"], label="Humidity")
plt.plot(df["Day"], df["Rainfall"], label="Rainfall")

plt.title("Weekly Weather Dashboard")
plt.xlabel("Day")
plt.ylabel("Weather Measurements")
plt.legend()

plt.show()

