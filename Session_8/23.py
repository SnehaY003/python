class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book = input("Book Name: ")
        self.books.append(book)

    def search_book(self):
        book = input("Enter Book Name: ")
        if book in self.books:
            print("Book Available")
        else:
            print("Book Not Found")

    def borrow_book(self):
        book = input("Enter Book Name: ")
        if book in self.books:
            self.books.remove(book)
            print("Book Borrowed")
        else:
            print("Book Not Available")

    def return_book(self):
        book = input("Enter Book Name: ")
        self.books.append(book)
        print("Book Returned")

l = Library()
while True:
    print("\n1.Add 2.Search 3.Borrow 4.Return 5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        l.add_book()
    elif ch == "2":
        l.search_book()
    elif ch == "3":
        l.borrow_book()
    elif ch == "4":
        l.return_book()
    elif ch == "5":
        break