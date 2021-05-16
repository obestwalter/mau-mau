import logging

from mau_mau.objects import Hand
from mau_mau.strategies import BasicStrategy

log = logging.getLogger(__name__)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand: Hand = Hand()
        self.strategy = BasicStrategy(self)

    def __repr__(self):
        name = self.__class__.__name__
        return f"{name}('{self.name}', {self.hand})"

    def __eq__(self, other):
        return self.name == other.name

    def play(self, table):
        self.strategy.play(table)
