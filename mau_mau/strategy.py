import logging

import collections
import random


log = logging.getLogger(__name__)


class BasicStrategy:
    def __init__(self, player):
        self.player = player

    def play(self, table):
        rule = table.rule
        log.debug("encountered rule %s", rule)
        if rule.skipPlayer:
            rule.skipPlayer = False
            log.debug("Damn. I can't play!")
            return

        card = None
        if rule.find_antidotes:
            card = self.before_play(table)
        self._play(table, card)

    def before_play(self, table):
        antidote = self.choose_antidote(
            table.rule.find_antidotes, self.antidote_strategy,
            self.player.hand)

        if not antidote:
            while len(table.rule.punishments):
                table.rule.punishments.pop()(self.player, table)
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

    def _play(self, table, card=None):
        rule = table.rule
        candidates = rule.find_playable_cards(self.player.hand)
        if not card:
            log.debug("find card to play")
            if candidates:
                card = self.choose_best_candidate(candidates)

        if card:
            assert card in candidates, (card, candidates)
            table.play_card(card, self.player.hand, self)
            return

        log.debug("nothing to play")
        rule.no_play_action(self.player, table)

    # noinspection PyUnusedLocal
    @classmethod
    def choose_best_candidate(cls, cards, *args, **kwargs):
        """Not much of a strategy here :)"""
        return cards[0]

    @property
    def wantedSuit(self):
        """The suit the Player wants as upcard, if he could choose"""
        counter = collections.Counter([c.suit for c in self.player.hand])
        # returns list of tuples [(value, count), (value, count), ...]
        # this slice simply picks the most common value
        return counter.most_common(1)[0][0]


class HumanStrategy(BasicStrategy):
    @classmethod
    def choose_antidote(cls, find_antidotes, antidotes_strategy, cards):
        allowedAntidotes = find_antidotes(cards)
        if not allowedAntidotes:
            log.info("no antidotes. Just take the punishment ...")
            return

        return cls.get_valid_choice(allowedAntidotes, "choose antidote")

    @classmethod
    def choose_best_candidate(cls, cards, *args, **kwargs):
        return cls.get_valid_choice(cards, "choose card to play")

    # fixme player is asked repeatedly if others can't play
    # add a buffer that saves the choice until the card is played
    @property
    def wantedSuit(self):
        from mau_mau import cardroom

        return self.get_valid_choice(cardroom.DECK.SUITS, "choose wanted suit")

    @classmethod
    def get_valid_choice(cls, choices, msg):
        def visu(elems):
            c = ["%s -> %s" % (i, c) for i, c in enumerate(elems, 1)]
            return " | ".join(c)

        while True:
            idx = input("%s.\n%s | " % (msg, visu(choices)))
            try:
                return choices[int(idx) - 1]

            except IndexError:
                log.warning("'%s' is not a valid choice", idx)
