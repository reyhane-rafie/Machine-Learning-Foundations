# 5. Password Validator
# Rules
# Minimum
#     • 8 characters 
#     • contains a number 
#     • contains a capital letter 
# (No regular expressions.)
# Practice
#     • loops 
#     • strings 
#     • booleans 
#     • functions 
# -------------------

def validate_password(password):
    long_enough = False
    has_number = False
    has_upper = False
   
    if len(password) >= 8:
        long_enough = True

    for charecter in password:
        if charecter.isdigit():
            has_number = True

        if charecter.isupper():
            has_upper = True

    if long_enough and has_number and has_upper:
        return True
    else: 
        return False

       

password = input("Enter password: ")

if validate_password(password):
    print("Valid password")
else:
    print("Invalid password")

