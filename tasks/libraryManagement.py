class LibraryOfBooks:
    def __init__(self):
        self.books = []
        self.numberOfBooks = 0

    def addBook(self, book):
        self.books.append(book)
        self.numberOfBooks = len(self.books)

    def showBooks(self):
        print(f"The Library has: {self.numberOfBooks} Books, The books are:")
        for book in self.books:
            print(book)

library = LibraryOfBooks()
library.addBook("Avengers: Endgame")
library.addBook("Avengers: Infinity War")
library.addBook("The Avengers")
library.showBooks()