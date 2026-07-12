def minimum(element):
    return min(element)


num= []
for i in range(1, 6):
    num.append(float(input(f"Enter element {i}: ")))
print("Minimum =", minimum(num))