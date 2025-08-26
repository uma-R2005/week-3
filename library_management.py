class Book:
    def __init__(self, id, title, author, genre):
        self.id, self.title, self.author, self.genre = id, title, author, genre
        self.issued = False
    def __str__(self):
        return f"{self.id}: {self.title} by {self.author} [{self.genre}] - {'Issued' if self.issued else 'Available'}"

class Member:
    def __init__(self, id, name):
        self.id, self.name, self.books = id, name, []
    def __str__(self):
        return f"{self.id}: {self.name} (Books: {len(self.books)})"

# Pre-existing books and members
books = [
    Book("B001", "1984", "George Orwell", "Dystopian"),
    Book("B002", "To Kill a Mockingbird", "Harper Lee", "Classic"),
    Book("B003", "The Great Gatsby", "F. Scott Fitzgerald", "Classic")
]

members = [
    Member("M001", "Alice"),
    Member("M002", "Bob")
]

while True:
    cmd = input("\nChoose: add_book, add_member, issue, return, list_books, list_members, exit\n> ").strip()
    if cmd == 'add_book':
        b = Book(input("ID: "), input("Title: "), input("Author: "), input("Genre: "))
        books.append(b)
        print("Book added.")
    elif cmd == 'add_member':
        m = Member(input("ID: "), input("Name: "))
        members.append(m)
        print("Member added.")
    elif cmd == 'issue':
        mid, bid = input("Member ID: "), input("Book ID: ")
        m = next((x for x in members if x.id == mid), None)
        b = next((x for x in books if x.id == bid), None)
        if not m or not b:
            print("Member or Book not found.")
        elif b.issued:
            print("Book already issued.")
        else:
            b.issued = True
            m.books.append(b)
            print("Book issued.")
    elif cmd == 'return':
        mid, bid = input("Member ID: "), input("Book ID: ")
        m = next((x for x in members if x.id == mid), None)
        if not m:
            print("Member not found.")
            continue
        b = next((x for x in m.books if x.id == bid), None)
        if not b:
            print("Book not issued to this member.")
        else:
            b.issued = False
            m.books.remove(b)
            print("Book returned.")
    elif cmd == 'list_books':
        for b in books:
            print(b)
        if not books:
            print("No books.")
    elif cmd == 'list_members':
        for m in members:
            print(m)
        if not members:
            print("No members.")
    elif cmd == 'exit':
        print("Bye!")
        break
    else:
        print("Unknown command.")
