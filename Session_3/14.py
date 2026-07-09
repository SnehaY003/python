N=int(input("Enter N: "))
old=N
rev=0
while N>0:
    i=N%10
    rev = rev * 10 + i
    N //= 10
if(old==rev):
    print("palindrome")
else:
    print("not palindrome")