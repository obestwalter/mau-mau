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
        return "%s(%s, %s)" % (name, self.rules, self.players)

    def join(self, players):
        """Players join at the table and therefore learn who comes next

        ... in a different program this would have a very different meaning
        """
        self.players = players
        for idx, player in enumerate(self.players):
            try:
                player.nextPlayer = players[idx + 1]
            except IndexError:
                player.nextPlayer = players[0]

    @staticmethod
    def transfer_punishments(sourceRule, destinationRule):
        for punishment in sourceRule.punishments:
            destinationRule.punishments.append(punishment)

    def replenish_stock(self):
        self.stock = Stock(self.waste)
        self.waste = Waste()
        self.stock.shuffle()

    @property
    def winner(self):
        try:
            return [p for p in self.players if self.rules.wins(p.hand)][0]

        except IndexError:
            return None


class Stock(_CardCollection):
    """technically not necessary but then it's clear what this represents"""
    pass


class Waste(_CardCollection):
    """technically not necessary but then it's clear what this represents"""
    pass


class Hand(_CardCollection):
    """technically not necessary but then it's clear what this represents"""
    pass


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        name = self.__class__.__name__
        return "%s('%s', '%s')" % (name, self.value, self.suit)
