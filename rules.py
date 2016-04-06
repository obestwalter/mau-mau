"""
* upcard is being fitted with extra rule objects dependent on special cards
* different kind of rule objects expectinng different reactions
* propagation conditions (e.g. out another 7 on and attach two more "draw conditions")
* no-play-condition -> default is draw, but would be empty on 8
* rules van be stacked ([draw, draw]),

 vague ideas ...
# rules and conditions as rule methods

* take a player as argument and return a card?
* the rule uses the strategy of the player and its hand to determine the action?


#####

Maybe it is a better idea to only add a rule object to the upcard if
the rule is special

this rule object is then active in the next turn and removed from the upcard
after it did it job. Adding a rule object with e.g. a suit wish as as part of
the jack would then be part of the players strategy.

Reacting to special rules like a seven which can be retaliated or not is also
part of the players strategy. The player checks the rule on the upcard to see
what he has to do (not put a card town for the eight, draw two), there should
also be a retaliation condition, which defines how to prevent having to stick
to the rule (putting a 7 on another seven and then adding two to the cards
that need to be drawn).
"""
import logging


log = logging.getLogger(__name__)


class DECK:
    SEVEN = 7
    EIGHT = 8
    JACK = 'Jack'
    VALUES = [SEVEN, EIGHT, 9, 10, JACK, 'Queen', 'King', 'Ace']
    SUITS = ['diamonds', 'hearts', 'spades', 'clubs']


def get_rule(value):
    if value == DECK.SEVEN:
        return RuleForSeven()

    if value == DECK.EIGHT:
        return RulesForEight()

    if value == DECK.JACK:
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
        if table.upcard.value != DECK.SEVEN:
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
