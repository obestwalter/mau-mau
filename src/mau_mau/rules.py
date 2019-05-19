import logging

from mau_mau.constants import DECK

log = logging.getLogger(__name__)


class BasicRule:
    def __init__(self, card, ruleClass):
        self.card = card
        self.rules = ruleClass
        self.strategy = None
        """If a player plays a card, they attach a strategy to their rule"""
        self.skipPlayer = False
        """Is active if a rule leads to a player being skipped"""
        self.find_antidotes = None
        """Contains a function to find an antidote if rules offers it"""
        self.punishments = []
        """One or several functions that execute punishments for the rule.

        If punishments are not prevented with an antidote or executed, they
        are propagated to the next rule.
        """

    def __repr__(self):
        name = self.__class__.__name__
        return f"{name} on {self.card}"

    def find_playable_cards(self, cards):
        return self.rules.find_playable_cards(self.card, cards)

    def no_play_action(self, player, table):
        return self.rules.no_play_action(player, table)


class MakePlayerDrawTwoCards(BasicRule):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.find_antidotes = self._find_antidotes
        self.punishments = [self._punishment]

    @staticmethod
    def _find_antidotes(cards):
        return [c for c in cards if c.value == DECK.SEVEN]

    @staticmethod
    def _punishment(player, table):
        player.draw(table, amount=2)


class SkipNextPlayer(BasicRule):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skipPlayer = True


class DemandWantedSuit(BasicRule):
    def find_playable_cards(self, cards):
        try:
            wantedSuit = self.strategy.wantedSuit
        except AttributeError:
            # No strategy attached -> First card in game
            wantedSuit = self.card.suit
        return [c for c in cards if c.suit == wantedSuit and not c.value == DECK.JACK]


class MauMau:
    RULES = {
        DECK.SEVEN: MakePlayerDrawTwoCards,
        DECK.EIGHT: SkipNextPlayer,
        DECK.JACK: DemandWantedSuit,
    }

    def __init__(self, cardsPerPlayer=5):
        self.cardsPerPlayer = cardsPerPlayer

    def __repr__(self):
        name = self.__class__.__name__
        return f"{name}({self.cardsPerPlayer})"

    @classmethod
    def get_rule(cls, card):
        RuleClass = cls.RULES.get(card.value, BasicRule)
        return RuleClass(card, cls)

    @staticmethod
    def find_playable_cards(upcard, cards):
        """Determines when a card is playable on the upcard"""
        return [
            c
            for c in cards
            if upcard.value == c.value or upcard.suit == c.suit or c.value == DECK.JACK
        ]

    @staticmethod
    def no_play_action(player, table):
        """Determines what a player has to do, if they don't play a card.

        :player Player: player that can't play
        :table Table: The game table
        """
        player.draw(table)

    @staticmethod
    def wins(cards):
        return cards is not None and len(cards) == 0
