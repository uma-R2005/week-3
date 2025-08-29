class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        if title in self.books:
            raise ValueError("Book already exists in library")
        self.books.append(title)

    def remove_book(self, title):
        if title not in self.books:
            raise ValueError("Book not found in library")
        self.books.remove(title)

    def search_book(self, title):
        return title in self.books

    def total_books(self):
        return len(self.books)
