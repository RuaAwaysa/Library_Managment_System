from exceptions.item_not_found import ItemNotFoundError
from exceptions.item_not_avilable import ItemNotAvailableError
from exceptions.user_not_found import UserNotFoundError
import json
from models.user import User
from models.book import Book
from models.dvd import DVD
from models.magazine import Magazine


class Library:
    def __init__(self):
        self.items = {}
        self.users = {}

    def view_available_items(self):
        for item in self.items.values():
            item.displayInfo()
        
    def view_all_users(self):
        for user in self.users.values():
            user.display_info()
            

    def add_item(self, item):
        self.items[item.item_id] = item

    def add_user(self,user):
        self.users[user.user_id] = user

    # check if the item borrowed by some one 
    def remove_item(self,item_id):
        if item_id not in self.items:
            raise ItemNotFoundError()
        
        for user in self.users.values():
            if item_id in user.borrowed_items:
                user.borrowed_items.remove(item_id)
        # Use del keyword to remove item with specified key
        del self.items[item_id]

    def remove_user(self,user_id):
        if user_id not in self.users:
            raise UserNotFoundError(f"User with ID {user_id} cannot be found to be deleted")
        user = self.users[user_id]
        for item_id in user.borrowed_items[:]:
            item = self.items.get(item_id)
            self.return_item(user_id,item_id)       
        del self.users[user_id]


    def borrow_item(self, user_id, item_id):
        # check if the user existt and the item exisit and not reserved 
        # if yes raise error if no so we can reserve it 
        # we will call the reserve atribute to the reserve the book or item for this user
        # the add the item to the borrowed item list of the user with id user_id
        #and change the status in the items and users dectionary
        user = self.users.get(user_id)
        item = self.items.get(item_id)
        if not user:
            raise UserNotFoundError()
        if not item:
            raise ItemNotFoundError
        if not item.check_availability():
            raise ItemNotAvailableError()
        item.reserve(user_id)
        item.available = False
        user.borrow_item(item_id)

    
    def return_item(self, user_id, item_id):
        user = self.users.get(user_id)
        item = self.items.get(item_id)
        if not user:
            raise UserNotFoundError()
        if not item:
            raise ItemNotFoundError()
        if item_id not in user.borrowed_items:
            raise ItemNotFoundError("This item not borrowe by this user")
        item.available = True
        item.reserved_by = None
        user.borrowed_items.remove(item_id)
        
        
    # Load the user data and the items data from the json files
    def load_data(self, users_file, items_file):
        try:
            with open(users_file,"r") as f:
                users_data = json.load(f)
                if not users_data:
                    raise ValueError("File is empty.")
                for item in users_data:
                    user = User(item['name'], item['email'])
                    user.user_id = item['user_id']
                    user.borrowed_items = item.get('borrowed_items',[])
                    self.users[user.user_id] = user
            with open(items_file,"r") as items:
                items_data = json.load(items)
                for item in items_data:
                    item_type = item.get('type')
                    if item_type == "Book":
                        obj = Book(item['title'],item['author'],item['year'],item['pages'],item['genre'],item['publisher'])
                    if item_type == "DVD":
                        obj = DVD(item['title'], item['author'], item['year'], item['genre'], item['duration'], item['rating'])
                    if item_type == "Magazine":
                        obj = Magazine(item['title'], item['author'], item['year'], item['issue'], item['category'], item['editor'], item['publisher'])
                    obj.item_id = item['item_id']
                    obj.available = item.get('available', True)
                    obj.reserved_by = item.get('reserved_by')
                    self.items[obj.item_id] = obj

        except FileNotFoundError:
            print("Error: File does not exist.")
        except ValueError as ve:
            print("Error:", ve)
        except TypeError:
            print("Error: Invalid operation on file.")
        except Exception as e:
            print(f"Error loading data: {e}")
        finally:
            try:
                f.close()
                print("Data loaded successfully")
                print("File closed successfully.")
            except NameError:
                print("File was never opened, so nothing to close.")

    def save_data(self,users_file, items_file):
        if not self.items:
            print("Warning: No items to save. Avoid overwriting the file with an empty list.")

        try: 
            with open(items_file, 'w') as f:
                item_data = [item.to_dict() for item in self.items.values()]
                json.dump(item_data, f, indent=2)
                
            with open (users_file,'w')as u:
                json.dump([user.to_dict() for user in self.users.values()],u,indent=2)

        except FileNotFoundError:
            print("Error: File does not exist.")
        except ValueError as ve:
            print("Error:", ve)
        except TypeError:
            print("Error: Invalid operation on file.")
        except Exception as e:
            print(f"Error saving data: {e}")
        finally:
            try:
                f.close()
                u.close()
                print("Files closed successfully.")
                print("Data Saved Successfully.")
            except NameError:
                print("File was never opened, so nothing to close.")
    
    def search_item(self,keyword):
        keyword = keyword.lower()
        Found = False
        for item in self.items.values():
            if keyword in item.title.lower() or keyword in item.__class__.__name__.lower():
                item.displayInfo()
                print("-" * 40)
                Found = True
        if not Found:
            print("No matches item pleas check you input.")

    def search_user(self, keyword):
        keyword = keyword.lower()
        found = False
        for user in self.users.values():
            if keyword in user.user_id.lower() or keyword in user.name.lower():
                user.display_info()
                print("-" * 40)
                found = True              
        if not found:
            raise UserNotFoundError("No user found matching the search.")

        
