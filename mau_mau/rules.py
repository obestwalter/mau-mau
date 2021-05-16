import logging

from mau_mau import functions
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


class MakePlayerDrawTwoCards(BasicRule):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.find_antidotes = self._find_antidotes
        self.punishments = [self._punishment]

    @staticmethod
    def _find_antidotes(cards):
        return [c for c in cards if c[0] == DECK.SEVEN]

    @staticmethod
    def _punishment(player, table):
        table.stock, table.waste = functions.draw(
            player, table.stock, table.waste, amount=2
        )


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
            wantedSuit = self.card[1]
        return [
            c
            for c in cards
            if c[1] == wantedSuit and not c[0] == DECK.JACK
        ]


class MauMau:
    SPECIAL_RULES = {
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
        RuleClass = cls.SPECIAL_RULES.get(card[0], BasicRule)
        return RuleClass(card, cls)

    @staticmethod
    def find_playable_cards(upcard, cards):
        """Determines when a card is playable on the upcard"""
        return [
            c
            for c in cards
            if upcard[0] == c[0]
            or upcard[1] == c[1]
            or c[0] == DECK.JACK
        ]

