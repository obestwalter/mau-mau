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
        return DrawTwo

    if value == DECK.EIGHT:
        return BlockFromPLaying

    if value == DECK.JACK:
        return ForceNewSuit

    return Rule


class Rule:
    """Rules the player has to adhere to.

    Is attached to the upcard.
    """
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def find_compatible_cards(self, cards):
        """Find all cards that could be played

        :cards list of Card: The hand of the player looking for an antidote
        :rtype: list of Card
        """
        return [c for c in cards if
                c.value == self.value or c.suit == self.suit]

    def punishment(self, player, table):
        """Defined as function call(s).

        If the player does not have an antidote or chooses not to use it, they
        have to call this function with themselves and the table as parameters
        and the punishment will be carried out *muhahahahaharrrr*

        :player Player: The player who deserves to be punished
        :table Table: The game table
        """

    def find_antidotes(self, cards):
        """Find cards that can prevent the punishment (empty if there is none)

        :cards list of Card: The hand of the player looking for an antidote
        :rtype: list of Card
        """
        return []

    def no_play_action(self, player, table):
        """The action that happens if the player does not put down a card.

        :player Player: player that can't play
        :table Table: The game table
        """
        player.draw_card(table.stock)

    @property
    def accumulates(self):
        """Does rule accumulate if player can't play?

        :rtype: bool
        """
        return False


class DrawTwo(Rule):
    def punishment(self, player, table):
        player.draw_card(table.stock)
        player.draw_card(table.stock)

    def find_antidotes(self, cards):
        return [c for c in cards if c.value == DECK.SEVEN]

    @property
    def accumulates(self):
        return True


class BlockFromPLaying(Rule):
    def find_compatible_cards(self, cards):
        return []

    def find_antidotes(self, cards):
        return []

    def no_play_action(self, player, table):
        pass

    @property
    def accumulates(self):
        return False


class ForceNewSuit(Rule):
    def find_compatible_cards(self, cards):
        return [c for c in cards if c.suit == self.strategy.wantedSuit]

    def find_antidotes(self, cards):
        return []

    @property
    def accumulates(self):
        return True
