# 44. GPA Progress Chart
# Input semester GPAs.
# Plot GPA through time.
# Practice
#     • line chart
# ------------------------

import matplotlib.pyplot as plt

semesters = ["S1", "S2", "S3", "S4", "S5", "S6"]
gpas = [14.2, 15.0, 14.7, 15.6, 16.1, 15.8]

plt.plot(semesters, gpas, marker="o")

plt.title("GPA Progress Across Semesters")
plt.xlabel("Semester")
plt.ylabel("GPA")

plt.show()

# Key lesson: An overall trend describes the general direction of the data, not necessarily what happens at every individual step.