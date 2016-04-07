import logging

import collections

from rules import NeedsNoAntidote, DefaultRule

log = logging.getLogger(__name__)


class Strategy:
    def __init__(self, player):
        self.player = player

    def play(self, table):
        rule = table.upcard.rule
        log.info("encountered rule %s", rule)
        assert isinstance(rule, DefaultRule)
        candidate = None
        try:
            log.debug("look for antidote")
            antidotes = rule.find_antidotes(self.player.hand)
            if antidotes:
                candidate = self.choose_antidote(rule, antidotes)
            else:
                log.debug("execute punishments")
                rule.execute_all_punishments(self.player, table)
        except NeedsNoAntidote:
            pass

        if not candidate:
            log.debug("no punishment necessary")
            candidates = rule.find_compatible_cards(self.player.hand)
            if candidates:
                candidate = self.choose_best_candidate(candidates)

        if not candidate:
            log.debug("not putting anything on %s", table.upcard)
            table.draw_from_stock(self.player)
            return

        card = self.player.hand.pop(self.player.hand.index(candidate))
        table.play_card(card, self)

    # noinspection PyUnusedLocal,PyMethodMayBeStatic
    def choose_best_candidate(self, candidates, *args, **kwargs):
        """Take first you can find. If it's a Jack ask for the same suit"""
        candidate = candidates[0]
        return candidate

    @property
    def wantedSuit(self):
        """The suit where Player has the most of"""
        counter = collections.Counter([c.suit for c in self.player.hand])
        # returns list of tuples [(value, count), (value, count), ...]
        # this slice simply picks the most common value
        return counter.most_common(1)[0][0]

    @staticmethod
    def choose_antidote(rule, antidotes):
        antidote = antidotes[0]
        log.debug("use %s against %s", antidote, rule)
        return antidote
