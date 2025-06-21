from models.library_item import LibraryItem
from models.reservable import Reservable
import uuid

class DVD(LibraryItem, Reservable):
    def __init__(self, title, author, year, genre, duration, rating):
        self.item_id = f"D-{str(uuid.uuid4())[:6]}"
        super().__init__(title, author, year)
        self.genre = genre
        self.duration = duration
        self.rating = rating
        self.available = True
        self.reserved_by = None

    def displayInfo(self):
        status = "Available" if self.available else "Borrowed"
        print(f"[DVD] {self.title}")
        print(f"ID: {self.item_id}")
        print(f"Director: {self.author}")
        print(f"Year: {self.year}")
        print(f"Duration: {self.duration}")
        print(f"Rating: {self.rating}")
        if self.reserved_by:
            print(f"Reserved by: {self.reserved_by}")
        else: 
            print("Reserved By: None")
        print(f"Status: {status}")
        print("-" * 40)

    def reserve(self, user_id):
        if self.reserved_by:
            raise Exception("This DVD is already reserved.")  # Replace later with custom exception
        self.reserved_by = user_id

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "type": "DVD",
            "genre": self.genre,
            "duration": self.duration,
            "rating": self.rating,
            "available": self.available,
            "reserved_by": self.reserved_by
        })
        return base
