class Book:
    def __init__(self, title, author, copies=1):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"📖 You borrowed '{self.title}'. Copies left: {self.copies}")
            return True
        else:
            print(f"❌ Sorry, '{self.title}' is currently unavailable.")
            return False

    def return_book(self):
        self.copies += 1
        print(f"📚 You returned '{self.title}'. Copies available now: {self.copies}")

    def book_info(self):
        print(f"\nTitle: {self.title}")
        print(f"Author: {self.author}")
        print(f"Copies Available: {self.copies}")

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.title in self.books:
            self.books[book.title].copies += book.copies
            print(f"➕ Added {book.copies} more copies of '{book.title}'.")
        else:
            self.books[book.title] = book
            print(f"➕ Added new book '{book.title}' to the library.")

    def borrow(self, title):
        if title in self.books:
            return self.books[title].borrow_book()
        else:
            print(f"❌ Book '{title}' not found in the library.")
            return False

    def return_book(self, title):
        if title in self.books:
            self.books[title].return_book()
        else:
            print(f"❌ Book '{title}' not found in the library.")

    def show_books(self):
        if not self.books:
            print("📚 No books in the library yet.")
            return
        print("\n📚 Library Books:")
        for book in self.books.values():
            book.book_info()

# === Demo ===
if __name__ == "__main__":
    library = Library()

    # Add books
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 3))
    library.add_book(Book("1984", "George Orwell", 2))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 2))  # Add copies

    library.show_books()

    # Borrow and return
    library.borrow("1984")
    library.borrow("The Great Gatsby")  # Not in library
    library.return_book("1984")

    library.show_books()
