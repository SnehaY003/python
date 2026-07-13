def set_operations(set1,set2):
    print("Union:", set1.union(set2))
    print("Intersection:", set1.intersection(set2))
    print("Difference:", set1.difference(set2))

set1=set()
set2=set()

n1=int(input("Enter number of elements in first set: "))
for i in range(n1):
    num=int(input("Enter element: "))
    set1.add(num)

n2=int(input("Enter number of elements in second set: "))
for i in range(n2):
    num=int(input("Enter element: "))
    set2.add(num)

set_operations(set1,set2)