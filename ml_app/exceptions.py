class Error(Exception):
    """
    Base class for custom exceptions
    """
    pass


class PreprocessingException(Error):
    """
    Raised when error occurs while preprocessing data
    """
    pass