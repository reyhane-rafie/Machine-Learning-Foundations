# 43. NDVI Histogram
# Generate NDVI values.
# Plot histogram.
# Interpret vegetation distribution.
# Practice
#     • histogram
#     • NumPy
#     • Matplotlib
# -------------------------------------

import numpy as np
import matplotlib.pyplot as plt

ndvi = np.random.normal(0.5, 0.15, 1000)

plt.hist(ndvi, bins=20)

plt.title("NDVI Distribution")
plt.xlabel("NDVI")
plt.ylabel("Number of Pixels")

plt.show()

