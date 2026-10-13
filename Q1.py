
# Username Validation System

username = input("Enter your username: ")

username = username.strip()

if username == "":
    print("Invalid username: It cannot contain only spaces.")

elif len(username) < 5:
    print("Invalid username: It must contain at least 5 characters.")

elif username.lower() == "admin":
    print("Invalid username: The username cannot be admin.")

else:
    print("Valid username!")
