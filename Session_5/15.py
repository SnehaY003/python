a=[]
n=int(input("Enter number of elements: "))

for i in range(n):
    a.append(int(input("Enter element: ")))

for item in set(a):
    print(item, "is", a.count(item),"times")