# 41. Monthly Expense Dashboard
# Visualize
#     • Spending by category
#     • Monthly spending trend
# Charts
#     • Bar chart
#     • Pie chart
# Practice
#     • Matplotlib
# ----------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
expenses = pd.read_csv("expenses-41.csv")

# Convert Date to datetime
expenses["Date"] = pd.to_datetime(expenses["Date"])


# --------------------------------
# 1. Spending by Category
# --------------------------------

category_spending = expenses.groupby("Category")["Amount"].sum()

print("\n--- Spending by Category ---")
print(category_spending)

category_spending.plot(kind="bar")

plt.title("Spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# --------------------------------
# 2. Monthly Spending Trend
# --------------------------------

expenses["Month"] = expenses["Date"].dt.to_period("M")

monthly_spending = expenses.groupby("Month")["Amount"].sum()

print("\n--- Monthly Spending ---")
print(monthly_spending)

monthly_spending.plot(kind="line", marker="o")

plt.title("Monthly Spending Trend")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()


# --------------------------------
# 3. Spending Distribution
# --------------------------------

category_spending.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Spending Distribution by Category")
plt.ylabel("")
plt.tight_layout()
plt.show()