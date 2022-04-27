class NoUrlError(Exception):
    "An exception raised when no url is provided"
    pass

class NoTokenProvided(Exception):
    "Exception raised when the auth token is not provided"
    pass