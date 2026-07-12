def SI(p,r,t):
    return (p*r*t)/100

p=float(input("Principal: "))
r=float(input("Rate: "))
t=float(input("Time: "))
print("Simple Interest =",SI(p, r, t))