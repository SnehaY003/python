def sort_list(a):
    print("Ascending:",sorted(a))
    print("Descending:",sorted(a[::-1]))

a=[]

n=int(input("Enter number of elements: "))

for i in range(n):
    num=int(input("Enter element: "))
    a.append(num)

sort_list(a)