class UserNotFoundError(Exception):
    def __init__(self, message="The user ID provided does not exist."):
        super().__init__(message)
