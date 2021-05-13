import logging

from mau_mau.concepts import _CardCollection

log = logging.getLogger(__name__)


class Table:
    def __init__(self):
        self.stock = None
        self.waste = None
        self.upcard = None
        self.players = None
        self.rules = None
        self.rule = None
        """active rule"""

    def __repr__(self):
        name = self.__class__.__name__
        return f"{name}({self.rules}, {self.players})"

    def join(self, players):
        """Players join the table and therefore learn who comes next

        ... not to be confused with joining tables in a database :)
        """
        self.players = players
        for idx, player in enumerate(self.players):
            try:
                player.nextPlayer = players[idx + 1]
            except IndexError:
                player.nextPlayer = players[0]

    @staticmethod
    def transfer_punishments(sourceRule, destinationRule):
        destinationRule.punishments.extend(sourceRule.punishments)

    def replenish_stock(self):
        self.stock = Stock(self.waste)
        self.waste = Waste()
        self.stock.shuffle()


class Stock(_CardCollection):
    """technically not necessary but then it's clear what this represents"""


class Waste(_CardCollection):
    """technically not necessary but then it's clear what this represents"""


class Hand(_CardCollection):
    """technically not necessary but then it's clear what this represents"""
