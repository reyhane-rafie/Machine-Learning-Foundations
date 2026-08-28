# 38. Water Quality Analyzer
# CSV contains
# pH
# Turbidity
# DO
# Classify each row.
# Count
#     • Good
#     • Moderate
#     • Poor
# Practice
#     • apply()
#     • DataFrame
# ----------------------------

import pandas as pd

water = pd.read_csv("water_quality.csv")

def classify_water(row):
    if 6.5 <= row["pH"] <= 8.5 and row["Turbidity"] < 5 and row["DO"] >= 6:
        return "Good"
    
    elif 6 <= row["pH"] <= 9 and row["Turbidity"] < 10 and row["DO"] >= 4:
        return "Moderate"
    
    else: 
        return "Poor"
    
water["Quality"] = water.apply(classify_water, axis=1)

good = (water["Quality"] == "Good").sum()

moderate = (water["Quality"] == "Moderate").sum()

poor = (water["Quality"] == "Poor").sum()

print("\n--- Water Quality Results ---")

print(water)

print("\nGood:", good)
print("Moderate:", moderate)
print("Poor:", poor)