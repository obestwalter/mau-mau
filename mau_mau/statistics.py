import logging
from statistics import mean
from timeit import timeit

from mau_mau import rules, play

log = logging.getLogger(__name__)


def mean_turns(players=3, reps=1000):
    games = _simulate_games(players, reps)
    log.info("mean turns played: %s", mean([g.turns for g in games]))


def winner_distribution(players=('Eric', 'Terry', 'John'), reps=1000):
    games = _simulate_games(players, reps)
    wc = {}
    # not optimal but premature optimization is the root of all evil ...
    for name in players:
        wc[name] = len([g for g in games if g.table.winner.name == name])
    log.info("winner distribution: %s", wc)


def time_durations(number=1000):
    timing = timeit(
        setup="from mau_mau.play import play_game;"
              "from mau_mau.rules import MauMau;"
              "mmRules = MauMau()",
        stmt="play_game(mmRules, 3)",
        number=number)
    log.info("it takes %0.3f seconds to play %s games", timing, number)


def _simulate_games(players, reps):
    log.info("players: %s; %s reps", players, reps)
    mmRules = rules.MauMau()
    games = []
    for i in range(reps):
        game = play.play_game(mmRules, players)
        games.append(game)
    return games
