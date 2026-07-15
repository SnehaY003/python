def check(num):
    if num < 0:
        raise ValueError("Negative number.")
    print("Number is positive.")

try:
    n = int(input("Enter number: "))
    check(n)

except ValueError as e:
    print(e)