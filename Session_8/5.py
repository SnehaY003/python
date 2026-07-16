class Calculator:
    def add(self, a,b):
        print("Addition =", a+b)

    def subtract(self, a, b):
        print("Subtraction =", a-b)

    def multiply(self, a, b):
        print("Multiplication =", a*b)

    def divide(self, a, b):
        print("Division =", a/b)

c = Calculator()
c.add(10, 5)
c.subtract(10, 5)
c.multiply(10, 5)
c.divide(10, 5)