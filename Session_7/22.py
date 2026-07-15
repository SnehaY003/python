balance = 1000
while True:
    print("\n----- Bank Management System -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                raise Exception("Invalid Amount")

            balance += amount
            print("Amount Deposited.")

        elif choice == 2:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                raise Exception("Invalid Amount")

            if amount > balance:
                raise Exception("Insufficient Balance")

            balance -= amount

            print("Withdrawal Successful.")

        elif choice == 3:
            print("Balance =", balance)

        elif choice == 4:
            print("Thank You")
            break

        else:
            print("Invalid Menu Choice")

    except ValueError:
        print("Enter numbers only.")

    except Exception as e:
        print(e)