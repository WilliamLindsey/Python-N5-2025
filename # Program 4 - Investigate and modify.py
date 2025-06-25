# Program 3 - Investigate and modify
password = input("Please enter your password: ")
while len(password) < 8 or len(password) > 20:
    if len(password) < 8:
        print("Must be longer than 8 characters.")
    elif len(password) > 20:
        print("Must be shorter than 20 characters.")
    password = input("Please enter your password: ")
print("Password accepted.")
