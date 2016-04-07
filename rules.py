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
        raise NeedsNoAntidote()

    def execute_punishment(self, player, table):
        """Defined as function call(s).

        If the player does not have an antidote or chooses not to use it, they
        have to call this function with themselves and the table as parameters
        and the punishment will be carried out *muhahahahaharrrr*

        :player Player: The player who deserves to be punished
        :table Table: The game table
        """

    def find_compatible_cards(self, cards):
        """Find all cards that could be played

        :cards list of Card: The hand of the player looking for an antidote
        :rtype: list of Card
        """
        return [c for c in cards if
                c.value == self.value or c.suit == self.suit]

    def no_play_action(self, player, table):
        """The action that happens if the player does not put down a card.

        :player Player: player that can't play
        :table Table: The game table
        """
        table.draw_from_stock(player)

    @property
    def propagates(self):
        """Does rule stay active if affected players can't play?

        :rtype: bool
        """
        return False


class DrawTwoCards(DefaultRule):
    def find_antidotes(self, cards):
        return [c for c in cards if c.value == DECK.SEVEN]

    def execute_punishment(self, player, table):
        table.draw_from_stock(player, amount=2)

    def no_play_action(self, player, table):
        """They do not have to draw because they already drew two"""
        pass

    @property
    def propagates(self):
        return True


class BlockPLayerFromPLaying(DefaultRule):
    def no_play_action(self, player, table):
        """They do not have to draw because they are skipped"""
        pass

    @property
    def propagates(self):
        return False


class DemandDifferentSuit(DefaultRule):
    def find_compatible_cards(self, cards):
        try:
            wantedSuit = self.strategy.wantedSuit
        except AttributeError:
            # No srategy attached -> First card in game
            wantedSuit = self.suit

        return [c for c in cards if c.suit == wantedSuit and
                not c.value == DECK.JACK]

    @property
    def propagates(self):
        return True
