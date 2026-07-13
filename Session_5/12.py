def remove_duplicates(a):
    new_list = []
    for item in a:
        if item not in new_list:
            new_list.append(item)
    return new_list

a = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num=int(input("Enter element: "))
    a.append(num)

print("List without duplicates:",remove_duplicates(a))