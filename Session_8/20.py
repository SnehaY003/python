class MathUtility:
    @staticmethod
    def factorial(n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print("Factorial =", fact)

    @staticmethod
    def prime(n):
        if n < 2:
            print("Not Prime")
            return

        for i in range(2, n):
            if n % i == 0:
                print("Not Prime")
                return
        print("Prime")

    @staticmethod
    def fibonacci(n):
        a = 0
        b = 1
        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b

MathUtility.factorial(5)
MathUtility.prime(7)
MathUtility.fibonacci(10)