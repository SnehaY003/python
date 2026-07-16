class Laptop:
    def __init__(self, brand, ram, processor, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Processor:", self.processor)
        print("Price:", self.price)


l = Laptop("Lenovo", "24GB", "Ryzen 5", 80000)
l.display()