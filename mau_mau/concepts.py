import logging

import collections
import random

log = logging.getLogger(__name__)


class Game:
    def __init__(self, table):
        self.table = table
        self.player = self.table.players[-1]
        self.turns = 0

    def __repr__(self):
        name = self.__class__.__name__
        return "%s(%s)" % (name, self.table)

    def next_turn(self):
        self.turns += 1
        self.player = self.player.nextPlayer
        log.debug("%s turn: %s %s" % ("-" * 45, self.turns, "-" * 45))
        log.debug("upcard: %s", self.table.upcard)
        log.debug("%s is up", self.player)
        return self.player

    @property
    def over(self):
        """should be named `isOver`. But then it wouldn't be game.over :)"""
        return self.table.winner is not None


class _Pile:
    """A collection of cards that are piled on top of each other"""
    def __init__(self, seed=None):
        """You can initialize the pile as empty with one card or a sequence"""
        if not seed:
            self.cards = []
        elif isinstance(seed, collections.Iterable):
            self.cards = seed
        else:
            self.cards = [seed]

    def __repr__(self):
        name = self.__class__.__name__
        return "%s(%s)" % (name, self.cards)

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        """Does not return anything: `random.shuffle` changes list in place"""
        random.shuffle(self.cards)
