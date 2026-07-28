# 15. Login System

# Store:
# Username
# Password

# Allow
# 3 attempts.

# After that
# Account Locked
# -----------------------

username = "admin"
password = "1234"

attempts = 0

print("=== Login System ===")

while attempts < 3:
    user = input("Username: ")
    pwd = input("Password: ")

    if user == username and pwd == password:
        print("Login successful!")
        break

    else:
        attempts += 1
        print("Incorrect username or password.")
        print("Attempts left:", 3 - attempts)
        
if attempts == 3:
    print("Account Locked")       