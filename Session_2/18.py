balance = 10000 
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice =int(input("Enter your choice: "))
if choice == 1:
    print("Balance =",balance)
elif choice == 2:
    amount = float(input("Enter amount: "))
    balance += amount
    print("New Balance =",balance)
elif choice == 3:
    amount = float(input("Enter amount: "))
    if amount <= balance:
        balance -= amount
        print("Remaining Balance =",balance)
    else:
        print("Insufficient Balance")
elif choice == 4:
    print("Exited")
else:
    print("Invalid Choice")