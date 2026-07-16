class Book:
    def __init__(self, book_id, title, author, price):
        self.bid= book_id
        self.title = title
        self.author = author
        self.price = price
    
    def display(self):
        print("Book Details")
        print("ID:", self.bid)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

b = Book(1, "Harry Potter", "JK Rowling", 2000)
b.display()
