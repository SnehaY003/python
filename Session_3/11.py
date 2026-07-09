N=int(input("Enter N: "))
cnt=0
while N>0:
    cnt+=1
    N//=10
print("Digits =", cnt)