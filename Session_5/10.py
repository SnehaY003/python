def search(a, key):
    if key in a:
        print("Element Found")
    else:
        print("Element Not Found")

a = []
elements = input("Enter list elements: ").split()

for i in elements:
    a.append(int(i))

key = int(input("Enter element to search: "))

search(a, key)