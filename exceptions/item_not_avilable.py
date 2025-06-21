class ItemNotAvailableError(Exception):
    def __init__(self,message="Item is not available for borrowing or reservation."):
        super().__init__(message)
