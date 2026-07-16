class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):
        for book in self.books:
            print(book)

l = Library()
l.add_book("Python")
l.add_book("Java")
l.add_book("Cpp")
l.view_books()