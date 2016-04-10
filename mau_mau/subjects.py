"""
TODO do sanity check after every round?

# ??? has the means to give to determine the winner
"""
import logging

from mau_mau import strategy
from mau_mau.cardroom import Card, Stock, Waste
from mau_mau.config import DECK


log = logging.getLogger(__name__)


class Croupier:
    def __init__(self):
        self._deck = None
        self._deckSize = 0

    def fetch_fresh_deck_of_cards(self):
        self._deck = [Card(v, s) for v in DECK.VALUES for s in DECK.SUITS]
        self._deckSize = len(self._deck)

    @staticmethod
    def deal_fresh_hand(player, stock, amount):
        player.hand = stock.fetch_cards(amount)
        log.debug("%s", player)

    def check_setup(self, players, cardsPerPlayer):
        assert len(players) > 1, "not enough players"
        neededCards = len(players) * cardsPerPlayer
        assert neededCards <= self._deckSize, "too many players"

    def check_table(self, table):
        assert table.upcard
        tableCardsLen = len(table.stock) + len(table.waste) + 1
        handsLen = sum(len(p.hand) for p in table.players if p.hand)
        assert tableCardsLen + handsLen == self._deckSize, \
            (tableCardsLen, handsLen, self._deckSize)

    @staticmethod
    def is_valid(value=None, suit=None):
        if not any([value, suit]):
            return False

        if value and value not in DECK.VALUES:
            return False

        if suit and suit not in DECK.VALUES:
            return False

        return True

    def set_table(self, table, rules):
        table.stock = Stock(self._deck)
        table.stock.shuffle()
        table.waste = Waste()
        table.upcard = table.stock.fetch_card()
        table.rule = rules.get_rule(table.upcard)


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
