# 1. Temperature Converter

# User chooses

# . Celsius → Fahrenheit
# . Fahrenheit → Celsius

# Use functions.

# Practice:

# input()
# if/else
# functions
# return 
# ----------------------------------
# Function: Celsius -> Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32

# Function: Fahrenheit -> Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print("1. Celsius → Fahrenheit")
print("2. Fahrenheit → Celsius")

choice = input("Choose an option (1 or 2): ")

if choice == "1":
    temperature = float(input("Enter the temperature in Celsius: "))
    result = celsius_to_fahrenheit(temperature)
    print("Temperature in Fahrenheit:", result)

elif choice == "2":
    temperature = float(input("Enter the temperature in Fahrenheit: "))
    result = fahrenheit_to_celsius(temperature)
    print("Temperature in Celsius:", result)

else:
    print("Invalid choice!")







