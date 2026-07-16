class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        amount = int(input("Enter Amount: "))
        self.balance += amount

    def withdraw(self):
        amount = int(input("Enter Amount: "))
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Balance =", self.balance)

b = Bank()
while True:
    print("\n1.Deposit 2.Withdraw 3.Check Balance 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        b.deposit()
    elif ch == "2":
        b.withdraw()
    elif ch == "3":
        b.check_balance()
    elif ch == "4":
        break