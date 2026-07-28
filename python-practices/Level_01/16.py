# 16. Rainfall Analyzer
# Input rainfall for:
# 30 days

# Output:
# Average rainfall

# Highest day

# Lowest day

# Dry days
# --------------

rainfall = []

def average_rainfall(rainfall):
    return sum(rainfall) / len(rainfall)

def highest_rainfall(rainfall):
    return max(rainfall)

def lowest_rainfall(rainfall):
    return min(rainfall)

def dry_days(rainfall):
    count = 0

    for amount in rainfall:
        if amount == 0:
            count += 1

    return count

for day in range(1, 31):
    amount = float(input(f"Day {day} rainfall (mm): "))

    rainfall.append(amount)

print("Average Rainfall:", average_rainfall(rainfall)) 
print("Highest Rainfall:", highest_rainfall(rainfall))
print("Lowest Rainfall:", lowest_rainfall(rainfall))
print("Dry Days:", dry_days(rainfall))           