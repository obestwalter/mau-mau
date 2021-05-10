class MauMauException(Exception):
    """All custom exceptions inherit from this"""


class NoCardsLeft(MauMauException):
    """Raised when trying to draw from empty collection of cards"""


class CardNotFound(MauMauException):
    """Raised when trying to draw from empty collection of cards"""
