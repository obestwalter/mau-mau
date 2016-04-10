"""
TODO do sanity check after every round?

# ??? has the means to give to determine the winner
"""
import logging

from mau_mau.config import DECK


log = logging.getLogger(__name__)


class Croupier:
    # def __init__(self, rules, players, stock):
    #     self.rules = rules
    #     self.players = players
    #     self.stock = stock

    @staticmethod
    def deal_fresh_hand(player, stock, amount):
        player.hand = stock.fetch_cards(amount)
        log.debug("%s", player)

    @staticmethod
    def ensure_setup_ok(players, cardsPerPlayer):
        assert len(players) > 1
        neededCards = len(players) * cardsPerPlayer
        assert neededCards <= len(DECK())

    @staticmethod
    def check_table(table):
        assert table.upcard
        tableCardsLen = len(table.stock) + len(table.waste) + 1
        handsLen = sum(len(p.hand) for p in table.players if p.hand)
        assert tableCardsLen + handsLen == len(DECK()), \
            (tableCardsLen, handsLen, len(DECK()))

    @staticmethod
    def is_valid(value=None, suit=None):
        if not any([value, suit]):
            return False

        if value and value not in DECK.VALUES:
            return False

        if suit and suit not in DECK.VALUES:
            return False

        return True
