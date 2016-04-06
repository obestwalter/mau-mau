import collections


class Strategy:
    def __init__(self, player, table):
        self.player = player
        self.table = table

        self.hand = self.player.hand

    # noinspection PyUnusedLocal,PyMethodMayBeStatic
    def choose_best_candidate(self, candidates, *args, **kwargs):
        """Take first you can find. If it's a Jack ask for the same suit"""
        candidate = candidates[0]
        return candidate

    @property
    def wantedSuit(self, cards):
        """The suit where Player has the most of"""
        counter = collections.Counter([c.suit for c in cards])
        # returns list of tuples [(value, count), (value, count), ...]
        # this slice simply picks the most common value
        return counter.most_common(1)[0][0]
