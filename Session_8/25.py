class Book:
    def __init__(self, title):
        self.title = title

    def display(self):
        print("Book:", self.title)

class EBook(Book):
    def display(self):
        print("EBook:", self.title)

class PrintedBook(Book):
    def display(self):
        print("Printed Book:", self.title)

b1 = EBook("Python Basics")
b2 = PrintedBook("Java Programming")
b1.display()
b2.display()