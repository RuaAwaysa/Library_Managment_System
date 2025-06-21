from models.library import Library
from models.user import User
from exceptions.user_not_found import UserNotFoundError
from exceptions.item_not_found import ItemNotFoundError
from exceptions.item_not_avilable import ItemNotAvailableError
import json
from models.book import Book
from models.dvd import DVD
from models.magazine import Magazine
class Main:
    def __init__(self):
        self.library = Library()
        self.users_file = "users.json"
        self.items_file = "items.json"
        self.library.load_data(self.users_file, self.items_file)
    
    def run(self):
        try:
            while True:
                self.display_menu()
                choice = input("Enter your choice (1-7): ").strip()
                if choice == "1":
                        self.library.view_available_items()

                elif choice == "2":
                        keyword = input("Enter a title or type (Book, DVD, Magazine): ").strip()
                        self.library.search_item(keyword)

                elif choice == "3":
                        self.register_user()

                elif choice == "4":
                        self.borrow_item()

                elif choice == "5":
                        self.return_item()
                
                elif choice == "6":
                    self.delete_user()

                elif choice == "7":
                    self.delete_item()

                elif choice == "8":
                    self.library.view_all_users()

                elif choice =="9":
                    self.add_new_item()
        
                elif choice == "10":
                    keyword = input("Enter user ID or part of name: ").strip()
                    try:
                        self.library.search_user(keyword)
                    except UserNotFoundError as e:
                        print(e)

                elif choice == "11":
                    self.exit_and_save()
                    break

                else:
                    print("Invalid choice. Please enter a number between 1 and 7.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user (Ctrl+C). Exiting...")
        except Exception as e:
            print(f"Unexpected error: {e}")
            print("Exiting program.")

    def delete_user(self):
        user_id = input("Enter user ID to delete: ").strip()
        try:
            self.library.remove_user(user_id)
            print("User removed successfully.")
        except UserNotFoundError as e:
            print(f"Error:{e}")
    
    def delete_item(self):
        item_id = input("Enter item ID to delete: ").strip()
        try:
            self.library.remove_item(item_id)
            print("Item removed successfully.")
        except ItemNotFoundError as e:
            print(f"{e}")
    
    def add_new_item(self):
        print("What type of item do you want to add?")
        print("1. Book")
        print("2. DVD")
        print("3. Magazine")
        choice = input("Enter your choice: ").strip()
        
        title = input("Title: ").strip()
        author = input("Author: ").strip()
        year = input("Year: ").strip()

        if choice == "1":
            pages = int(input("Pages: "))
            genre = input("Genre: ").strip()
            publisher = input("Publisher: ").strip()
            book = Book(title, author, year, pages, genre, publisher)
            self.library.add_item(book)
            print("New Book with title {title} added successfully.")
        
        elif choice == "2":
            genre = input("Genre: ").strip()
            duration = input("Duration (e.g., 2h 30m): ").strip()
            rating = input("Rating: ").strip()
            dvd = DVD(title, author, year, genre, duration, rating)
            self.library.add_item(dvd)
            print("DVD with title {title} added successfully.")
        
        elif choice == "3":
            issue = input("Issue Date (e.g., April 2024): ").strip()
            category = input("Category: ").strip()
            editor = input("Editor: ").strip()
            publisher = input("Publisher: ").strip()
            magazine = Magazine(title, author, year, issue, category, editor, publisher)
            self.library.add_item(magazine)
            print("Magazine with title {title} added successfully.")
        
        else:
            print("Invalid type.")

    def register_user(self):
        name = input("Enter your name: ").strip()
        email = input("Enter your email: ").strip()
        user = User(name, email)
        self.library.add_user(user)
        print(f"User registered successfully! Your user ID is: {user.user_id}")

    def borrow_item(self):
        user_id = input("Enter your user ID: ").strip()
        item_id = input("Enter item ID to borrow: ").strip()
        try:
            self.library.borrow_item(user_id, item_id)
            print("Item borrowed successfully.")
        except (UserNotFoundError, ItemNotFoundError, ItemNotAvailableError) as e:
            print(f"error: {e}")
    
    def return_item(self):
        user_id = input("Enter your user ID: ").strip()
        item_id = input("Enter item ID to return: ").strip()
        try:
            self.library.return_item(user_id, item_id)
            print("Item returned successfully.")
        except (UserNotFoundError, ItemNotFoundError) as e:
            print(f"{e}")
    
    def exit_and_save(self):
        print("Items before saving:", len(self.library.items))
        self.library.save_data(self.users_file, self.items_file)
        # print("Data saved. Exiting system. Goodbye")
    
        
    def display_menu(self):
        print("\n📚 Welcome to the Library System")
        print("1. View all available items")
        print("2. Search item by title or type")
        print("3. Register as a new user")
        print("4. Borrow an item")
        print("5. Return an item")
        print("6. Delete a user")
        print("7. Delete an item")
        print("8. View all users")
        print("9. Add a new item")
        print("10. Search for user by name or ID")
        print("11. Exit and Save")
    
# Entry point
if __name__ == "__main__":
    Main().run()
