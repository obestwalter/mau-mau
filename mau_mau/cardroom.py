import logging

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


class Table:
    def __init__(self):
        self.rules = None
        self.players = None
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

    def play_card(self, card, hand, strategy):
        log.debug("play %s", card)
        card = hand.pop(hand.index(card))
        self.waste.put_card(self.upcard)
        self.upcard = card
        oldRule = self.rule
        self.rule = self.rules.get_rule(card)
        self.rule.strategy = strategy
        self.transfer_punishments(oldRule, self.rule)

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

    @property
    def winner(self):
        try:
            return [p for p in self.players if self.rules.wins(p.hand)][0]

        except IndexError:
            return None


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
