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


class PredictionException(Error):
    """
    Raised when error occurs while generating predictions
    """
    pass