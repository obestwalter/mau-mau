import logging
from numbers import Integral

import collections
import random

from mau_mau import exc

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
        log.debug("%s turn %s %s" % ("-" * 20, self.turns, "-" * 20))
        log.debug("upcard: %s", self.table.upcard)
        log.debug("%s is up", self.player)
        return self.player

    @property
    def over(self):
        """should be named `isOver`. But then it wouldn't be game.over :)"""
        return self.table.winner is not None


class _CardCollection:
    """A sequence of cards, used for all groups of cards used in the game."""
    def __init__(self, seed=None):
        """Pile can be initialized with different seed kinds"""
        if not seed:
            self.cards = []
        elif isinstance(seed, _CardCollection):
            self.cards = seed.cards
        elif isinstance(seed, collections.Iterable):
            self.cards = seed
        else:
            self.cards = [seed]

    def __repr__(self):
        """Nice automatic representation for all inheriting objects.

        >>> from mau_mau.objects import Stock
        >>> s = Stock([1, 2, 3])
        >>> repr(s)
        'Stock([1, 2, 3])'
        """
        name = self.__class__.__name__
        return "%s(%s)" % (name, self.cards)

    def __len__(self):
        """Object has a length that is the number of cards contained in it.

        >>> c = _CardCollection([1, 2, 3])
        >>> len(c)
        3

        >>> c = _CardCollection()
        >>> not c
        True
        """
        return len(self.cards)

    def __iter__(self):
        """Let's me use the object like a genuine Python sequence

        >>> [e for e in _CardCollection([1, 2, 3])]
        [1, 2, 3]
        """
        for card in self.cards:
            yield card

    def shuffle(self):
        """Does not return anything: `random.shuffle` changes list in place"""
        random.shuffle(self.cards)

    def put(self, card):
        self.cards.append(card)

    def fetch(self, criterion=None):
        """Fetch one ore several cards from the collection.

        * Given (None, 0, 1): fetch first card from the collection
        * Given a specific card: fetch that specific card
        * Given a number > 1: return a list of cards
        :rtype: Card or list of Card
        """
        if not self.cards:
            raise exc.NoCardsLeft()

        try:
            if not criterion or criterion == 1:
                return self.cards.pop(0)

            if isinstance(criterion, Integral):
                return [self.cards.pop(i) for i in range(criterion)]

            return self.cards.pop(self.cards.index(criterion))
        except (IndexError, ValueError):
            raise exc.CardNotFound()
