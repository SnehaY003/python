try:
    num=int(input("Enter a number: "))

except ValueError:
    print("Please enter valid integer.")

else:
    print("Square =",num*num)