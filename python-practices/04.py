# 4. Guess the Secret Number
# Computer stores
# secret = 17
# User keeps guessing until correct.
# Output
# Too high
# Too low
# Correct!
# Practice
#     • while 
#     • if 
#     • break 
# -------------------
# Random number
# ++++++++++
# import random

# secret = random.randint(1, 20)
# +++++++++++
secret = 17

while True:
    guess = int(input("Guess The Number : "))

    if guess == secret:
       print("Correct!")
       break

    elif guess > secret:
        print("Too high")

    elif guess < secret:
        print("Too low")    

