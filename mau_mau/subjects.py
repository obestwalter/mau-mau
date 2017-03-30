import collections
import logging

from mau_mau.const import DECK
from mau_mau.objects import Stock, Waste, Hand, Card
from mau_mau.strategy import HumanStrategy, BasicStrategy

log = logging.getLogger(__name__)


class Croupier:
    """Prepares everything to get the game going

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

    def set_table(self, table, rules):
        table.rules = rules
        table.stock = Stock(self._deck)
        table.stock.shuffle()
        table.waste = Waste()
        table.upcard = table.stock.fetch()
        table.rule = rules.get_rule(table.upcard)


class Player:
    def __init__(self, name, strategyClass=BasicStrategy):
        self.name = name
        self.hand = Hand()
        """:type: Hand"""
        self.strategy = strategyClass(self)
        self.nextPlayer = None

    def __repr__(self):
        name = self.__class__.__name__
        return "%s('%s', %s)" % (name, self.name, self.hand)

    def __eq__(self, other):
        return self.name == other.name

    def play(self, table):
        self.strategy.play(table)

    def draw(self, table, amount=1):
        for _ in range(amount):
            if not table.stock:
                table.replenish_stock()
            card = table.stock.fetch()
            self.hand.put(card)
            log.debug("%s <- %s" % (self.name, card))

    def put(self, table, card, strategy):
        log.debug("play %s", card)
        card = self.hand.fetch(card)
        table.waste.put(table.upcard)
        table.upcard = card
        oldRule = table.rule
        table.rule = table.rules.get_rule(card)
        table.rule.strategy = strategy
        table.transfer_punishments(oldRule, table.rule)
