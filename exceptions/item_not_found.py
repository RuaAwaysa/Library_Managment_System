class ItemNotFoundError(Exception):
    def __init__(self, message="The requested item was not found in the system."):
        super().__init__(message)
