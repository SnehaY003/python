class car:
    def __init__(self, brand, model, year):
        self.br=brand
        self.m=model
        self.yr=year

    def display(self):
        print("Car Details:")
        print("Brand:", self.br)
        print("Model:", self.m)
        print("Year:", self.yr)

c = car("Toyota", "Fortuner", 2022)
c.display()