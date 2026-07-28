# 10. Number Statistics
# User enters numbers until typing
# done
# Show
# Maximum

# Minimum

# Average

# Count
# -----------------------

numbers = []

def maximum(numbers):
    return max(numbers)

def minimum(numbers):
    return min(numbers)

def average(numbers):
    return sum(numbers) / len(numbers)

def count_numbers(numbers):
    return len(numbers)

while True:
    value = input("Enter number: ")

    if value == "done":
        break 

    else:
        number = float(value)
        numbers.append(number)

if len(numbers) > 0:
    print("Maximum:", maximum(numbers))
    print("Minimum:", minimum(numbers))
    print("Average:", average(numbers))
    print("Count:", count_numbers(numbers))
else:
    print("No numbers were entered.")
