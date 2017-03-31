import logging
import sys
from statistics import mean
from timeit import timeit

import fire

from mau_mau import rules, play
from mau_mau.constants import LOG

log = logging.getLogger()


class Statistics:
    def turns(self, players=3, reps=1000):
        """calculate mean turns for <reps> games of <players>"""
        games = self._simulate_games(players, reps)
        log.info("mean turns played: %s", mean([g.turns for g in games]))

    def winners(self, players=('Eric', 'Terry', 'John'), reps=1000):
        """calculate winner distribution for <reps> <players>"""
        games = self._simulate_games(players, reps)
        wc = {}
        # not optimal but premature optimization is the root of all evil ...
        for name in players:
            wc[name] = len([g for g in games if g.table.winner.name == name])
        log.info("winner distribution: %s", wc)

    def durations(self, reps=1000):
        """calculate durations for <reps> games"""
        timing = timeit(
            setup="from mau_mau.play import play_game;"
                  "from mau_mau.rules import MauMau;"
                  "mmRules = MauMau()",
            stmt="play_game(mmRules, 3)",
            number=reps)
        log.info("it takes %0.3f seconds to play %s games", timing, reps)

    def _simulate_games(self, players, reps):
        log.info("players: %s; %s reps", players, reps)
        mmRules = rules.MauMau()
        games = []
        for i in range(reps):
            game = play.play_game(mmRules, players)
            games.append(game)
        return games


def main():
    logging.basicConfig(format=LOG.FMT, level=logging.INFO)
    try:
        fire.Fire(Statistics)
    except KeyboardInterrupt:
        log.error("\nfatal: lost game by chickening out!")
        sys.exit(1)
