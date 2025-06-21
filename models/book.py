from models.library_item import LibraryItem
from exceptions.item_not_avilable import ItemNotAvailableError
import uuid
from models.reservable import Reservable
class Book(LibraryItem,Reservable):
    def __init__(self, title,author, year, pages ,genre,publisher):
        self.item_id = f"B-{str(uuid.uuid4())[:6]}"
        super().__init__(title, author, year)
        self.pages = pages
        self.genre = genre
        self.publisher = publisher
        self.year = year
        self.available = True
        self.reserved_by = None

    
    def displayInfo(self):
        status = "Available" if self.available else "Borrowed"
        print(f"[BOOK] {self.title}")
        print(f"ID: {self.item_id}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Pages: {self.pages}")
        print(f"Genre: {self.genre}")
        print(f"Publisher: {self.publisher}")
        if self.reserved_by:
            print(f"Reserved by: {self.reserved_by}")
        else: 
            print("Reserved By: None")
        print(f"Status: {status}")
        print("-" * 40)

    def reserve(self, user_id):
        if self.reserved_by:
            raise ItemNotAvailableError("This book is already reserved.")
        self.reserved_by = user_id
    
    def to_dict(self):
        base = super().to_dict()
        base.update({
            "type": "Book",
            "pages": self.pages,
            "genre": self.genre,
            "publisher": self.publisher,
            "available": self.available,
            "reserved_by": self.reserved_by
        })
        return base