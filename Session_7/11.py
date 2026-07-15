try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter (+,-,*,/): ")

    if op == "+":
        print(a + b)

    elif op == "-":
        print(a - b)

    elif op == "*":
        print(a * b)

    elif op == "/":
        print(a / b)

    else:
        print("Invalid operator.")

except ValueError:
    print("Enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")