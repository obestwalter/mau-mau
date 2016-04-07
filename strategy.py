import logging

import collections

from rules import NeedsNoAntidote, rule_class

log = logging.getLogger(__name__)


class Strategy:
    def __init__(self, player):
        self.player = player

    def play(self, table):
        rule = table.upcard.rule
        log.debug("encountered rule %s", rule)
        candidate = None
        try:
            log.debug("look for antidote")
            antidotes = rule.find_antidotes(self.player.hand)
            if antidotes:
                candidate = self.choose_antidote(rule, antidotes)
                log.debug("found antidote %s", candidate)
            else:
                rule.punish(self.player, table)
        except NeedsNoAntidote:
            log.debug("needs no antidote")

        if not candidate:
            log.debug("find card to play")
            candidates = rule.find_compatible_cards(self.player.hand)
            if candidates:
                candidate = self.choose_best_candidate(candidates)

        if not candidate:
            log.debug("nothing to play")
            rule.no_play_action(self.player, table)
            value = table.upcard.value
            suit = table.upcard.suit
            table.upcard.rule = rule_class(value)(value, suit)
            return

        table.play_card(self.player, candidate, self)

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
