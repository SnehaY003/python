try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)

except ValueError:
    print("Please enter valid integer.")