def maximum(element):
    return max(element)


num= []
for i in range(1, 6):
    num.append(float(input(f"Enter element {i}: ")))
print("Maximum =", maximum(num))