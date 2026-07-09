N=int(input("Enter N: "))
sum=0
while N>0:
    i=N%10
    sum+=i
    N//=10
print("Sum =", sum)