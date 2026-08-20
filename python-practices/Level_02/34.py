# 34. NDVI Array Analyzer
# Create a random NDVI image.
# Calculate
#     • Average NDVI
#     • Forest pixels
#     • Water pixels
# Practice
#     • Boolean masking
#     • NumPy
# ------------------------------

import numpy as np


ndvi = np.random.uniform(-1, 1, (5, 5))

print(ndvi)


average_ndvi = np.mean(ndvi)

water_mask = ndvi < 0
water_pixels = np.sum(water_mask)

forest_mask = ndvi > 0.5
forest_pixels = np.sum(forest_mask)


print("Average NDVI:", round(average_ndvi, 2))
print("Forest pixels:", forest_pixels)
print("Water pixels:", water_pixels)

