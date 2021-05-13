import logging
import random
from collections.abc import Iterable

from mau_mau import exceptions

log = logging.getLogger(__name__)


class _CardCollection:
    """A sequence of cards, used for all groups of cards used in the game."""

    def __init__(self, seed=None):
        """Can be initialized with different seed kinds"""
        if not seed:
            self.cards = []
        elif isinstance(seed, _CardCollection):
            self.cards = seed.cards
        elif isinstance(seed, Iterable):
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
        return f"{name}({self.cards})"

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

    def shuffle(self) -> None:
        """Does not return anything: `random.shuffle` changes list in place"""
        random.shuffle(self.cards)

    def put(self, card):
        self.cards.append(card)

    def fetch(self, criterion=None):
        """Fetch one or several cards from the collection.

        * Given (None, 0, 1): fetch first card from the collection
        * Given a specific card: fetch that specific card
        * Given a number > 1: return a list of cards
        :rtype: Card or list of Card
        """
        if not self.cards:
            raise exceptions.NoCardsLeft()

        try:
            if not criterion or criterion == 1:
                return self.cards.pop(0)

            if isinstance(criterion, int):
                return [self.cards.pop(i) for i in range(criterion)]

            return self.cards.pop(self.cards.index(criterion))
        except (IndexError, ValueError):
            raise exceptions.CardNotFound()
