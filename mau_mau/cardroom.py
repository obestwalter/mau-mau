import logging

import random

from mau_mau import strategy

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


class Player:
    def __init__(self, name, strategyClass=strategy.BasicStrategy):
        self.name = name
        self.hand = None
        self.strategy = strategyClass(self)
        self.nextPlayer = None

    def __repr__(self):
        name = self.__class__.__name__
        return "%s('%s', %s)" % (name, self.name, self.hand)

    def __eq__(self, other):
        return self.name == other.name

    def play_turn(self, table):
        self.strategy.play(table)


class Table:
    def __init__(self, rulesOfTheGame, players):
        self.rules = rulesOfTheGame
        self.players = players
        self.rule = None
        """active rule"""

    def __repr__(self):
        name = self.__class__.__name__
        return "%s(%s, %s)" % (name, self.rules, self.players)

    def set(self, deck):
        self.stock = Stock(deck)
        self.stock.shuffle()
        self.waste = Waste()
        self.upcard = self.stock.fetch_card()
        self.rule = self.rules.get_rule(self.upcard)
        self.check_setup_sanity()

    @property
    def winner(self):
        try:
            return [p for p in self.players if self.rules.wins(p.hand)][0]

        except IndexError:
            return None

    def deal_fresh_hand(self):
        for player in self.players:
            cards = self.stock.fetch_cards(self.rules.cardsPerPlayer)
            player.hand = cards
            log.debug("%s", player)
            self.check_table_sanity()

    def play_card(self, card, hand, strategy):
        log.debug("play %s", card)
        card = hand.pop(hand.index(card))
        self.waste.put_card(self.upcard)
        self.upcard = card
        oldRule = self.rule
        self.rule = self.rules.get_rule(card)
        self.rule.strategy = strategy
        self.transfer_punishments(oldRule, self.rule)
        self.check_table_sanity()

    def draw_from_stock(self, hand, amount=1):
        for _ in range(amount):
            self.ensure_stock_is_replenished()
            card = self.stock.fetch_card()
            hand.append(card)
            log.debug(card)

    @staticmethod
    def transfer_punishments(sourceRule, destinationRule):
        for punishment in sourceRule.punishments:
            destinationRule.punishments.append(punishment)

    def ensure_stock_is_replenished(self):
        if self.stock.isEmpty:
            self.stock = Stock(self.waste.cards)
            self.waste = Waste()
            self.stock.shuffle()
            self.check_table_sanity()

    def check_setup_sanity(self):
        assert len(self.players) > 1
        neededCards = len(self.players) * self.rules.cardsPerPlayer
        assert neededCards <= len(DECK())

    def check_table_sanity(self):
        assert self.upcard
        tableCardsLen = len(self.stock) + len(self.waste) + 1
        handsLen = sum(len(p.hand) for p in self.players if p.hand)
        assert tableCardsLen + handsLen == len(DECK()), \
            (tableCardsLen, handsLen, len(DECK()))


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


class DECK:
    SEVEN = 7
    EIGHT = 8
    JACK = 'Jack'
    VALUES = [SEVEN, EIGHT, 9, 10, JACK, 'Queen', 'King', 'Ace']
    SUITS = ['♦', '♥', '♠', '♣']

    def __init__(self):
        self.len = len(self.make_initializers())

    @classmethod
    def make_initializers(cls):
        return [(v, s) for v in cls.VALUES for s in cls.SUITS]

    @classmethod
    def create(cls):
        return [Card(*i) for i in cls.make_initializers()]

    def __len__(self):
        return self.len
