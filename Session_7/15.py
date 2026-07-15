try:
    email = input("Enter Email: ")
    if "@" not in email:
        print("Invalid Email")

    elif "." not in email:
        print("Invalid Email")

    elif " " in email:
        print("Spaces are not allowed")

    else:
        print("Email is valid")

except:
    print("Invalid Input")