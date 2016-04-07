import logging

import random

from strategy import Strategy


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
        log.debug("%s is up (turn %s)", self.player, self.turns)

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
    def __init__(self, name, strategyClass=Strategy):
        self.name = name
        self.hand = None
        self.strategy = strategyClass(self)

    def __repr__(self):
        name = self.__class__.__name__
        return "%s('%s', %s)" % (name, self.name, self.hand)

    def __eq__(self, other):
        return self.name == other.name

    @property
    def hasWon(self):
        return len(self.hand) == 0

    def play_turn(self, table):
        self.strategy.play(table)

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

    def ensure_stock_is_replenished(self):
        if self.stock.isEmpty:
            self.stock = Stock(self.waste.cards)
            self.waste = Waste()
            self.stock.shuffle()

    def play_card(self, card):
        self.waste.append(self.upcard)
        self.upcard = card


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
    def __init__(self, *args, rule=None):
        self.value, self.suit = args
        self.rule = rule
        """:type: DefaultRule"""

    def __repr__(self):
        name = self.__class__.__name__
        return "%s('%s', '%s')" % (name, self.value, self.suit)
