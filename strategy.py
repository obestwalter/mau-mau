import logging

import collections

from rules import NeedsNoAntidote

log = logging.getLogger(__name__)


class Strategy:
    def __init__(self, player):
        self.player = player
        self.hand = self.player.hand

    def play(self, table):
        rule = table.upcard.rule
        candidate = None
        try:
            antidotes = rule.find_antidotes(self.hand)
            if antidotes:
                candidate = self.choose_antidote(rule, antidotes)
            else:
                rule.execute_punishment(self.player, table)
        except NeedsNoAntidote:
            pass

        if not candidate:
            candidates = rule.find_compatible_cards(self.hand)
            candidate = self.choose_best_candidate(candidates)

        if not candidate:
            log.info("not putting anything on %s", table.upcard)
            table.ensure_stock_is_replenished()
            self.player.draw_card()

        card = self.hand.pop(self.hand.index(candidate))
        log.info("puts %s on %s", card, table.upcard)
        table.waste.put_card(table.upcard)
        card.rule.strategy = self
        table.upcard = card

    # noinspection PyUnusedLocal,PyMethodMayBeStatic
    def choose_best_candidate(self, candidates, *args, **kwargs):
        """Take first you can find. If it's a Jack ask for the same suit"""
        candidate = candidates[0]
        return candidate

    @property
    def wantedSuit(self):
        """The suit where Player has the most of"""
        counter = collections.Counter([c.suit for c in self.hand])
        # returns list of tuples [(value, count), (value, count), ...]
        # this slice simply picks the most common value
        return counter.most_common(1)[0][0]

    @staticmethod
    def choose_antidote(rule, antidotes):
        antidote = antidotes[0]
        log.debug("use %s against %s", antidote, rule)
        return antidote
