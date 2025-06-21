import uuid
class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.user_id = f"U-{str(uuid.uuid4())[:6]}"
        self.borrowed_items=[]
    
    def display_info(self):
            print(f"User ID: {self.user_id}\nName: {self.name}\nEmail: {self.email}")
            print(f"Borrowed Items: {', '.join(self.borrowed_items) if self.borrowed_items else 'No Borrowed item'}\n")
            print("-" * 40)
    
    def borrow_item(self, item_id):
        if item_id in self.borrowed_items:
            print("Item already exisit in your borrowd list")
        self.borrowed_items.append(item_id)

    def return_item(self, item_id):
        if item_id in self.borrowed_items:
            self.borrowed_items.remove(item_id)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'borrowed_items': self.borrowed_items
        }