class Vehicle:
    def rent(self):
        print("Vehicle Rent")

class Car(Vehicle):
    def rent(self):
        print("Car Rent = 1000")

class Bike(Vehicle):
    def rent(self):
        print("Bike Rent = 500")

class Truck(Vehicle):
    def rent(self):
        print("Truck Rent = 2000")

c = Car()
b = Bike()
t = Truck()
c.rent()
b.rent()
t.rent()