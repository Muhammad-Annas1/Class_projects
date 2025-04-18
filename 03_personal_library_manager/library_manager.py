import json


class BookCollection:
   

    def __init__(self):
       
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
       
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
       
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
      
        book_title = input("Enter book title: ")
        book_author = input("Enter author: ")
        try:
            publication_year = int(input("Enter publication year: "))
        except ValueError:
            print("Invalid year. Please enter an integer.\n")
            return
        book_genre = input("Enter genre: ")
        is_book_read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }

        self.book_list.append(new_book)
        self.save_to_file()
        print("✅ Book added successfully!\n")

    def delete_book(self):
       
        book_title = input("Enter the title of the book to remove: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("✅ Book removed successfully!\n")
                return
        print("❌ Book not found!\n")

    def find_book(self):
        
        search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice: ").strip()
        search_text = input("Enter search term: ").lower()

        if search_type not in ["1", "2"]:
            print("❌ Invalid search option.\n")
            return

        if search_type == "1":
            found_books = [book for book in self.book_list if search_text in book["title"].lower()]
        else:
            found_books = [book for book in self.book_list if search_text in book["author"].lower()]

        if found_books:
            print("\n📚 Matching Books:")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(
                    f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
                )
        else:
            print("❌ No matching books found.\n")

    def update_book(self):
       
        book_title = input("Enter the title of the book you want to edit: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("Leave blank to keep existing value.")
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = input(f"New author ({book['author']}): ") or book["author"]
                try:
                    new_year = input(f"New year ({book['year']}): ")
                    if new_year:
                        book["year"] = int(new_year)
                except ValueError:
                    print("Invalid year. Skipping update for year.")

                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
                read_input = input("Have you read this book? (yes/no): ").strip().lower()
                if read_input in ["yes", "no"]:
                    book["read"] = read_input == "yes"

                self.save_to_file()
                print("✅ Book updated successfully!\n")
                return
        print("❌ Book not found!\n")

    def show_all_books(self):
        
        if not self.book_list:
            print("📭 Your collection is empty.\n")
            return

        print("\n📚 Your Book Collection:")
        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "Unread"
            print(
                f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
            )
        print()

    def show_reading_progress(self):
        
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (completed_books / total_books * 100) if total_books > 0 else 0
        print(f"\n📈 Reading Statistics:")
        print(f"Total books in collection: {total_books}")
        print(f"Books read: {completed_books}")
        print(f"Reading progress: {completion_rate:.2f}%\n")

    def show_menu(self):
        
        print("📘=== Book Collection Menu ===📘")
        print("1. Add a new book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Update book details")
        print("5. Display all books")
        print("6. Display statistics")
        print("7. Exit")

    def start_application(self):
       
        while True:
            self.show_menu()
            choice = input("Choose an option (1-7): ").strip()

            if choice == "1":
                self.create_new_book()
            elif choice == "2":
                self.delete_book()
            elif choice == "3":
                self.find_book()
            elif choice == "4":
                self.update_book()
            elif choice == "5":
                self.show_all_books()
            elif choice == "6":
                self.show_reading_progress()
            elif choice == "7":
                self.save_to_file()
                print("👋 Thank you for using Book Collection Manager. Goodbye!")
                break
            else:
                print("❌ Invalid option. Please try again.\n")


if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()
