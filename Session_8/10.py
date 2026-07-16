class MobilePhone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def call(self):
        print("Calling...")

    def send_message(self):
        print("Message Sent")

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


m = MobilePhone("Samsung", "A35")
m.display()
m.call()
m.send_message()