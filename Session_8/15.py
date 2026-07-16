class Customer:
    def __init__(self, customer_id, name, phone):
        self.cid = customer_id
        self.name = name
        self.phone = phone

    def display(self):
        print("Customer ID:", self.cid)
        print("Name:", self.name)
        print("Phone:", self.phone)

c = Customer(101, "Sneha", "XXXXXXXXXX")
c.display()