# 3. Grade Calculator
# Input
# Math
# Physics
# English
# Output
# Average: 17.3

# Grade: Excellent
# Rules
# 18-20 Excellent
# 16-18 Very Good
# 14-16 Good
# 12-14 Pass
# <12 Fail
# Practice
#     • conditions 
#     • arithmetic 
#     • functions 
# ------------------------------

# Function to determine the grade
def calculate_grade(average):
    if average >= 18:
        return "Excellent"
    elif average >= 16:
        return "Very Good"
    elif average >= 14:
        return "Good"
    elif average >= 12:
        return "Pass"
    else:
        return "Fail"


# Get user input
math = float(input("Enter your Math score: "))
physics = float(input("Enter your Physics score: "))
english = float(input("Enter your English score: "))

# Calculate the average
average = (math + physics + english) / 3

# Call the function
grade = calculate_grade(average)

# Display the results
print(f"Average: {average:.1f}")
print(f"Grade: {grade}")