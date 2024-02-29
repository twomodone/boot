class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for current_book in self.books:
            if(book.title == current_book.title and book.author == current_book.author):
               self.books.remove(current_book) 

    def search_books(self, search_string):
        matching_books = []
        for book in self.books:
            title = book.title.lower()
            author = book.author.lower()
            if (search_string.lower() in title or search_string.lower() in author):
                matching_books.append(book)
        return matching_books
