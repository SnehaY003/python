class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance+amount

    def withdraw(self, amount):
        self.balance = self.balance-amount

    def check_balance(self):
        print("Balance =", self.balance)

b = BankAccount()
b.deposit(5000)
b.withdraw(2000)
b.check_balance()