# 2. Even or Odd Checker

# User enters numbers repeatedly until typing "stop".

# Output

# 12 -> Even
# 5 -> Odd
# 17 -> Odd

# Practice

# while
# break
# functions
# ---------------------------------------
def even_or_odd(number):
    if number % 2 == 0:
        return('EVEN')
    else:   
        return('ODD') 

while True:
    user = input("Enter a number (or 'stop'): ")

    if user == 'stop':
        break

    number = int(user)
    result = even_or_odd(number)

    print(f"{number} -> {result}")