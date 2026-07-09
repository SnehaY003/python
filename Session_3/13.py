N = int(input("Enter a number: "))
reverse = 0
while N > 0:
    i = N % 10
    reverse = reverse * 10 + i
    N //= 10

print("Reverse =", reverse)