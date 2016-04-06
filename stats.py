import logging
from statistics import mean
from timeit import timeit

from sim import play_game

log = logging.getLogger(__name__)


def mean_turns(players=3, reps=10000):
    games = _simulate_games(players, reps)
    log.info("mean turns played: %s", mean([g.turns for g in games]))


def winner_distribution(players=('Eric', 'Terry', 'John'), reps=10000):
    games = _simulate_games(players, reps)
    wc = {}
    # not optimal but premature optimization os the course of all evil ...
    for name in players:
        wc[name] = len([g for g in games if g.winner.name == name])
    log.info("winner distribution: %s", wc)


def time_durations(number=10000):
    timing = timeit(stmt="play_game()",
                    setup="from sim import play_game",
                    number=number)
    log.info("%s playing games take %0.3f seconds", number, timing)


def _simulate_games(players, reps):
    log.info("players: %s; %s reps", players, reps)
    games = []
    for i in range(reps):
        game = play_game(players)
        games.append(game)
    return games
