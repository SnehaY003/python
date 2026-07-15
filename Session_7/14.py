try:
    password = input("Enter Password: ")

    upper = False
    lower = False
    digit = False

    for ch in password:
        if ch.isupper():
            upper = True

        if ch.islower():
            lower = True

        if ch.isdigit():
            digit = True

    if len(password) < 8:
        print("Password must contain at least 8 characters.")

    elif upper==False:
        print("Password must contain one uppercase letter.")

    elif lower==False:
        print("Password must contain one lowercase letter.")

    elif digit ==False:
        print("Password must contain one digit.")

    else:
        print("Password is valid.")

except:
    print("Invalid Input")