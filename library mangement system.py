class Library:
    def __init__(self):  # Fixed the method name from _init_ to __init__
        self.books = {}

    def add_book(self, title, author):
        """Add a book to the library."""
        self.books[title] = {'author': author, 'available': True}
        print(f'Added: "{title}" by {author}')

    def view_books(self):
        """Display all books and their availability."""
        print("\nAvailable Books:")
        if not self.books:
            print("No books in the library.")
            return
        for title, details in self.books.items():
            status = "Available" if details['available'] else "Lent Out"
            print(f'"{title}" by {details["author"]} - {status}')

    def lend_book(self, title):
        """Lend a book to a user."""
        if title in self.books:
            if self.books[title]['available']:
                self.books[title]['available'] = False
                print(f'You have lent "{title}". Enjoy reading!')
            else:
                print(f'Sorry, "{title}" is currently lent out.')
        else:
            print(f'Sorry, "{title}" is not in the library.')

    def run(self):
        """Run the library management system."""
        while True:
            print("\nLibrary Management System")
            print("1. Add Book")
            print("2. View Books")
            print("3. Lend Book")
            print("4. Exit")

            choice = input("Choose an option (1-4): ")

            if choice == '1':
                title = input("Enter the book title: ")
                author = input("Enter the author's name: ")
                self.add_book(title, author)
            elif choice == '2':
                self.view_books()
            elif choice == '3':
                title = input("Enter the title of the book to lend: ")
                self.lend_book(title)
            elif choice == '4':
                print("Exiting the library system. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

# Example usage
if __name__ == "__main__":
    library = Library()
    library.run()
