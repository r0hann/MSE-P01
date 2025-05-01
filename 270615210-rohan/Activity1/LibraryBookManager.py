class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

class LibraryManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added to the library.")

    def show_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            print("\nBooks in the library:")
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. ", end="")
                book.display_info()

# Main code
if __name__ == "__main__":
    library = LibraryManager()
    
    while True:
        print("\nLibrary Manager Menu:")
        print("1. Add a book")
        print("2. Show all books")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            library.add_book(title, author)
        elif choice == "2":
            library.show_books()
        elif choice == "3":
            print("Exiting the Library Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
