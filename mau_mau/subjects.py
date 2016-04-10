import logging

import collections

from mau_mau.config import DECK
from mau_mau.objects import Stock, Waste, Card
from mau_mau.strategy import HumanStrategy, BasicStrategy

log = logging.getLogger(__name__)


class Croupier:
    """Coordinates the game flow.

    * knows the rules and preconditions needed to play a game
    * can summon, manipulate and coordinate all needed subjects and objects
    """
    def __init__(self):
        self._deck = None
        self._deckSize = 0

    def fetch_fresh_deck_of_cards(self):
        self._deck = [Card(v, s) for v in DECK.VALUES for s in DECK.SUITS]
        self._deckSize = len(self._deck)

    @classmethod
    def invite(cls, seed, table):
        realPlayers = cls._create_real_players(seed)
        log.debug("invite %s to: %s", realPlayers, table)
        table.join(realPlayers)

    @classmethod
    def _create_real_players(cls, seed):
        """given an amount or some names magic some players out of thin air.

        :type seed: int or list of str
        """
        if not isinstance(seed, collections.Iterable):
            return [Player("Player %s" % (n)) for n in range(1, seed + 1)]

        rps = []
        for player in seed:
            s = HumanStrategy if player == 'human' else BasicStrategy
            rps.append(Player(player, s))
        return rps

    @classmethod
    def _tell_players_where_to_sit(cls, players):
        """So that players know who's next"""
        for idx, player in enumerate(players):
            try:
                player.nextPlayer = players[idx + 1]
            except IndexError:
                player.nextPlayer = players[0]

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
        table.rules = rules  # FIXME questionable if they belong there ...
        table.stock = Stock(self._deck)
        table.stock.shuffle()
        table.waste = Waste()
        table.upcard = table.stock.fetch_card()
        table.rule = rules.get_rule(table.upcard)


class Player:
    def __init__(self, name, strategyClass=BasicStrategy):
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
