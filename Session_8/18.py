class Number:

    @staticmethod
    def check(num):
        if num > 0:
            print("Positive Number")
        else:
            print("Negative Number")

n = int(input("Enter a number: "))
Number.check(n)