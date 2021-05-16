import logging

from mau_mau.objects import Hand

log = logging.getLogger(__name__)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand: Hand = Hand()

    def __repr__(self):
        name = self.__class__.__name__
        return f"{name}('{self.name}', {self.hand})"

    def __eq__(self, other):
        return self.name == other.name
