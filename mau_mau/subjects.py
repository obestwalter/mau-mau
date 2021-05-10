import logging

from mau_mau.objects import Hand
from mau_mau.strategies import BasicStrategy

log = logging.getLogger(__name__)


class Player:
    def __init__(self, name, strategyClass=BasicStrategy):
        self.name = name
        self.hand: Hand = Hand()
        self.strategy = strategyClass(self)
        self.nextPlayer = None
        """Will point to next player when players have joined a table"""

    def __repr__(self):
        name = self.__class__.__name__
        return f"{name}('{self.name}', {self.hand})"

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
            log.debug(f"{self.name} <- {card}")

    def put(self, table, card, strategy):
        log.debug(f"play {card}")
        card = self.hand.fetch(card)
        table.waste.put(table.upcard)
        table.upcard = card
        oldRule = table.rule
        table.rule = table.rules.get_rule(card)
        table.rule.strategy = strategy
        table.transfer_punishments(oldRule, table.rule)
