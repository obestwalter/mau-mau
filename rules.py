import logging


log = logging.getLogger(__name__)


class DECK:
    SEVEN = 7
    EIGHT = 8
    JACK = 'Jack'
    VALUES = [SEVEN, EIGHT, 9, 10, JACK, 'Queen', 'King', 'Ace']
    SUITS = ['diamonds', 'hearts', 'spades', 'clubs']


def rule_class(value):
    if value == DECK.SEVEN:
        return DrawTwoCards

    if value == DECK.EIGHT:
        return BlockPLayerFromPLaying

    if value == DECK.JACK:
        return DemandDifferentSuit

    return DefaultRule


class NeedsNoAntidote(Exception):
    pass


class DefaultRule:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.accumulation = 1

    def __repr__(self):
        name = self.__class__.__name__
        return "%s('%s', %s)" % (name, self.value, self.suit)

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def find_antidotes(self, cards):
        """Find cards that can prevent the punishment (empty if there is none)

        :cards list of Card: The hand of the player looking for an antidote
        :rtype: list of Card
        """
        raise NeedsNoAntidote(repr(self))

    def punish(self, player, table):
        """
        If the player does not have an antidote or chooses not to use it, they
        have to call this function with themselves and the table as parameters
        and the punishment will be carried out *muhahahahaharrrr*

        :player Player: The player who deserves to be punished
        :table Table: The game table
        """
        for idx in range(self.accumulation):
            log.debug("execute punishment %s", idx)
            self._punish(player, table)

    def _punish(self, player, table):
        """one concrete punishment - override this"""

    def find_compatible_cards(self, cards):
        """Find all cards that could be played

        :cards list of Card: The hand of the player looking for an antidote
        :rtype: list of Card
        """
        return [c for c in cards if
                c.value == self.value or c.suit == self.suit]

    def no_play_action(self, player, table):
        """What happens if the player does not put down a card.

        :player Player: player that can't play
        :table Table: The game table
        """
        table.draw_from_stock(player)


class DrawTwoCards(DefaultRule):
    def find_antidotes(self, cards):
        return [c for c in cards if c.value == DECK.SEVEN]

    def _punish(self, player, table):
        table.draw_from_stock(player, amount=2)


class BlockPLayerFromPLaying(DefaultRule):
    def find_compatible_cards(self, cards):
        return []

    def no_play_action(self, player, table):
        """no drawing, no accumulation"""


class DemandDifferentSuit(DefaultRule):
    def find_compatible_cards(self, cards):
        try:
            wantedSuit = self.strategy.wantedSuit
        except AttributeError:
            # No strategy attached -> First card in game
            wantedSuit = self.suit
        return [c for c in cards if c.suit == wantedSuit and
                not c.value == DECK.JACK]
