class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, discount):
        self.price = self.price - discount

    def display(self):
        print("Product:", self.name)
        print("Price:", self.price)


p = Product("Laptop", 50000)
p.apply_discount(5000)
p.display()