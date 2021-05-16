import collections
import logging
import random

from mau_mau import functions

log = logging.getLogger(__name__)


class BasicStrategy:
    def play(self, table, player):
        rule = table.rule
        log.debug("encountered rule %s", rule)
        if rule.skipPlayer:
            rule.skipPlayer = False
            log.debug("Damn. I can't play!")
            return

        card = None
        if rule.find_antidotes:
            card = self.before_play(table, player)
        self._play(table, player, card)

    def before_play(self, table, player):
        antidote = self.choose_antidote(
            table.rule.find_antidotes, self.antidote_strategy, player.hand
        )

        if not antidote:
            while table.rule.punishments:
                table.rule.punishments.pop()(player, table)
        return antidote

    @classmethod
    def choose_antidote(cls, find_antidotes, antidotes_strategy, cards):
        log.debug("find antidote")
        antidotes = find_antidotes(cards)
        if antidotes:
            antidote = antidotes_strategy(antidotes)
            log.debug("found antidote %s", antidote)
            return antidote

    # noinspection PyUnusedLocal
    @staticmethod
    def antidote_strategy(antidotes, *args, **kwargs):
        return random.choice(antidotes)

    def _play(self, table, player, card):
        rule = table.rule
        candidates = rule.find_playable_cards(player)
        if not card:
            log.debug("find card to play")
            if candidates:
                card = self.choose_best_candidate(candidates)

        if card:
            assert card in candidates, (card, candidates)

            log.debug(f"play {card}")
            card = player.hand.fetch(card)
            table.waste.put(table.upcard)
            table.upcard = card
            oldRule = table.rule
            table.rule = table.rules.get_rule(card)
            table.rule.strategy = self
            table.transfer_punishments(oldRule, table.rule)
            return

        log.debug("nothing to play")
        table.stock, table.waste = functions.draw(player, table.stock, table.waste)

    # noinspection PyUnusedLocal
    @classmethod
    def choose_best_candidate(cls, cards, *args, **kwargs):
        """Not much of a strategy here :)"""
        return cards[0]

    @staticmethod
    def wanted_suit(player):
        """The suit the Player wants as upcard, if he could choose"""
        counter = collections.Counter([c[1] for c in player.hand])
        # returns list of tuples [(value, count), (value, count), ...]
        # this slice simply picks the most common value
        return counter.most_common(1)[0][0]


# HumanStrategy had to go due to decomposition
