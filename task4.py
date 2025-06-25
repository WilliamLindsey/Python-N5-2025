age = float(input("Please enter your age:"))
if age < 0.0:
    print("You are not born yet!")
elif age < 18.0:
    print("You can't apply for a driving license.")
else:
    print("You can apply for a driving license.")