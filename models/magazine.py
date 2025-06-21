from models.library_item import LibraryItem
from exceptions.item_not_avilable import ItemNotAvailableError
import uuid

class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue, category, editor, publisher):
        self.item_id = f"M-{str(uuid.uuid4())[:6]}"
        super().__init__(title, author, year)
        self.issue = issue
        self.category = category
        self.editor = editor
        self.publisher = publisher
        self.available = True
        self.reserved_by = None

    def reserve(self, user_id):
        if self.reserved_by:
            raise ItemNotAvailableError("This book is already reserved.")
        self.reserved_by = user_id

    def displayInfo(self):
        status = "Available" if self.available else "Borrowed"
        
        print(f"[MAGAZINE] {self.title}")
        print(f"ID: {self.item_id}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Issue: {self.issue}")
        print(f"Category: {self.category}")
        print(f"Editor: {self.editor}")
        print(f"Publisher: {self.publisher}")
        if self.reserved_by:
            print(f"Reserved by: {self.reserved_by}")
        else: 
            print("Reserved By: None")
        print(f"Status: {status}")
        print("-" * 40)

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "type": "Magazine",
            "issue": self.issue,
            "category": self.category,
            "editor": self.editor,
            "publisher": self.publisher,
            "reserved_by": self.reserved_by,
            "reserved_by": self.reserved_by
        })
        return base
