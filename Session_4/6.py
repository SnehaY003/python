def even_or_odd(a):
    if(a%2==0):
        return "Even"
    else: return "odd"

num1=float(input("Enter first number: "))
print("",num1," is",even_or_odd(num1))