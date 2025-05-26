class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn


class Library(Book):
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)
        print(f"{self.books} added in the library")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"removed: {book.title}")
    
    def display_books(self):
        if not self.books:
            print("No books available")
        for book in self.books:
            status = "Available" if book else "Checked out"
            print(f"{book.title} - {status}")

book1 = Book("Crime thriller","Debayan","89000")
book2 = Book("Granther kabya","Kunal","89001")
book3 = Book("Fiction","Anindya","89002")
lib1 = Library()
lib1.add_books(book1)
lib1.add_books(book2)
lib1.add_books(book3)
lib1.remove_book("89000")
lib1.display_books()