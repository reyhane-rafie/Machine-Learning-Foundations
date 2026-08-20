# 35. Satellite Band Calculator
# Generate Red and NIR arrays.
# Calculate
# NDVI = (NIR-Red)/(NIR+Red)
# Display summary statistics.
# Practice
#     • NumPy
#     • scientific computing
# -------------------------------

import numpy as np

red = np.random.uniform(0.1, 0.8, (5, 5))

nir = np.random.uniform(0.1, 0.9, (5, 5))

print("Red Band:")
print(red)

print("\nNIR Band:")
print(nir)

ndvi = (nir - red) / (nir + red)

print("\nNDVI:")
print(np.round(ndvi, 2))

mean_ndvi = np.mean(ndvi)

min_ndvi = np.min(ndvi)

max_ndvi = np.max(ndvi)

std_ndvi = np.std(ndvi)

print("\n--- NDVI Summary ---")

print("Mean NDVI:", round(mean_ndvi, 2))
print("Minimum NDVI:", round(min_ndvi, 2))
print("Maximum NDVI:", round(max_ndvi, 2))
print("Standard Deviation:", round(std_ndvi, 2))