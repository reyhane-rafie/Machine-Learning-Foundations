# 32. Weather Statistics
# Generate temperatures for one year.
# Calculate
#     • Mean
#     • Median
#     • Standard deviation
#     • Maximum
#     • Minimum
# Practice
#     • NumPy
#     • statistics
# ---------------------------------------

import numpy as np
import statistics

temperatures = np.random.uniform(-5, 40, 365)
# Or: temperatures = np.random.randint(-5, 41, 365)

mean = np.mean(temperatures)
# Or: mean = statistics.mean(temperatures)

median = np.median(temperatures)
# Or: median = statistics.median(temperatures)

std = np.std(temperatures)
# Or: std = statistics.pstdev(temperatures)

maximum = np.max(temperatures)

minimum = np.min(temperatures)

print("Mean:", round(mean, 2))
print("Median:", round(median, 2))
print("Standard Deviation:", round(std, 2))
print("Maximum:", round(maximum, 2))
print("Minimum:", round(minimum, 2))
