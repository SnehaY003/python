class circle:
    def __init__(self, radius):
        self.rad = radius

    def area(self):
        print("Area =", 3.14*self.rad*self.rad)

    def circumference(self):
        print("Perimeter =", 2*3.14*self.rad)

r = circle(2)
r.area()
r.circumference()