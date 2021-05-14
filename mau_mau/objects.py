import logging

from mau_mau.concepts import _CardCollection

log = logging.getLogger(__name__)


class Table:
    def __init__(self):
        self.stock = None
        self.waste = None
        self.upcard = None
        self.rules = None
        self.rule = None
        """active rule"""

    def __repr__(self):
        name = self.__class__.__name__
        return f"{name}({self.rules})"

    @staticmethod
    def transfer_punishments(sourceRule, destinationRule):
        destinationRule.punishments.extend(sourceRule.punishments)


class Stock(_CardCollection):
    """technically not necessary but then it's clear what this represents"""


class Waste(_CardCollection):
    """technically not necessary but then it's clear what this represents"""


class Hand(_CardCollection):
    """technically not necessary but then it's clear what this represents"""
