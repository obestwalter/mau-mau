import logging

import random

log = logging.getLogger(__name__)


class Game:
    def __init__(self, gamers, table):
        self.gamers = gamers
        self.table = table
        self.player = self.gamers[-1]
        self.turns = 0

    def __repr__(self):
        name = self.__class__.__name__
        return "%s(%s, %s)" % (name, self.gamers, self.table)

    def next_turn(self):
        self.turns += 1
        try:
            currentPlayerIndex = self.gamers.index(self.player)
            self.player = self.gamers[currentPlayerIndex + 1]
        except IndexError:
            self.player = self.gamers[0]
        log.debug("-" * 120)
        log.debug("round %s - %s plays", self.turns, self.player.name)

    @property
    def over(self):
        """should be named `isOver`. But then it wouldn't be game.over :)"""
        return self.winner is not None

    @property
    def winner(self):
        try:
            return [p for p in self.gamers if p.hasWon][0]

        except IndexError:
            return None


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __repr__(self):
        name = self.__class__.__name__
        return "%s('%s', %s)" % (name, self.name, self.hand)

    def __eq__(self, other):
        return self.name == other.name

    @property
    def hasWon(self):
        return len(self.hand) == 0

    def play_card(self, gameCard):
        for card in self.hand:
            if card.is_playable(gameCard):
                return self.hand.pop(self.hand.index(card))

    def draw_card(self, stock):
        self.hand.append(stock.fetch_card())
        log.debug("%s drew %s", self.name, self.hand[-1])


class Table:
    def __init__(self, stock, waste, upcard):
        self.stock = stock
        self.waste = waste
        self.upcard = upcard

    def __repr__(self):
        name = self.__class__.__name__
        return "%s(%s, %s, %s)" % (name, self.stock, self.waste, self.upcard)


class _Pile:
    def __init__(self, seed=None):
        if not seed:
            self.cards = []
        elif isinstance(seed, Card):
            self.cards = [seed]
        else:
            self.cards = seed

    def __repr__(self):
        name = self.__class__.__name__
        return "%s(%s)" % (name, self.cards)

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        """Does not return anything: `random.shuffle` changes list in place"""
        random.shuffle(self.cards)


class Stock(_Pile):
    class StockEmpty(Exception):
        """Raised when trying to draw from empty pile"""

    def fetch_cards(self, amount):
        return [self.fetch_card() for _ in range(amount)]

    def fetch_card(self):
        try:
            return self.cards.pop(len(self.cards) - 1)

        except IndexError:
            raise self.StockEmpty()

    @property
    def isEmpty(self):
        return not len(self.cards)


class Waste(_Pile):
    def put_card(self, card):
        self.cards.append(card)


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        name = self.__class__.__name__
        return "%s('%s', '%s')" % (name, self.value, self.suit)

    def is_playable(self, otherCard):
        return self.suit == otherCard.suit or self.value == otherCard.value
