from abc import ABC , abstractmethod
class LibraryItem(ABC):
    def __init__(self,title,author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available  = True
    @abstractmethod
    def displayInfo(self):
        pass
    
    def check_availability(self):
        return self.available

    # For serialization into JSON format
    def to_dict(self):
        return {
            "item_id": getattr(self, "item_id", None),
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "available": self.available
        }