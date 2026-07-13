def operations(numbers):
    print("Maximum:",max(numbers))
    print("Minimum:",min(numbers))
    print("Sum:",sum(numbers))
    print("Average:",sum(numbers)/len(numbers))

numbers = []

print("Enter 10 numbers:")
for i in range(10):
    numbers.append(int(input()))

operations(numbers)