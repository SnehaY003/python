class Rectangle:
    def __init__(self, length, breadth):
        self.len = length
        self.bth = breadth

    def area(self):
        print("Area =", self.len*self.bth)

    def perimeter(self):
        print("Perimeter =", 2*(self.len+self.bth))

r = Rectangle(10,2)
r.area()
r.perimeter()