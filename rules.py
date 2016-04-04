import logging


log = logging.getLogger(__name__)


class DEF:
    SEVEN = 7
    EIGHT = 8
    JACK = 'Jack'
    VALUES = [SEVEN, EIGHT, 9, 10, JACK, 'Queen', 'King', 'Ace']
    SUITS = ['diamonds', 'hearts', 'spades', 'clubs']


def get_rule(value):
    if value == DEF.SEVEN:
        return RuleForSeven()

    if value == DEF.EIGHT:
        return RulesForEight()

    if value == DEF.JACK:
        return RulesForJack()

    return Rule()


# needs a notion of being active for seven and eight
# player after the one played must not draw or be skipped
# so should only be active for next player
class Rule:
    def cards_compatible(self, upcard, candidate):
        return upcard.suit == candidate.suit or candidate.value == upcard.value

    def post_play_action(self, *args, **kwargs):
        return


class RuleForSeven(Rule):
    def post_play_action(self, player, table):
        if table.upcard.value != DEF.SEVEN:
            player.draw_card()
            player.draw_card()


class RulesForEight(Rule):
    def cards_compatible(self, upcard, candidate):
        # FIXME must only be active for next player
        # see active notion of active above
        return False

    def post_play_action(self, player, table):
        log.info("%s is skipped", player.name)
        return


class RulesForJack(Rule):
    def __init__(self):
        self.wantedSuit = None

    def cards_compatible(self, card, upcard):
        if self.wantedSuit:
            return card.suit == self.wantedSuit

        return card.suit == upcard.suit
