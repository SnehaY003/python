try:
    age = int(input("Enter age: "))
    if age > 0 and age < 120:
        print("Age accepted")
    else:
        print("Enter valid Age!")

except ValueError:
    print("Invalid input")