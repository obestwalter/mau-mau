#!/usr/bin/env python3
"""
This module gives simple command line access to the functions.

Start it without parameters to run a simple game.

Start it with one of the functions in stat.py to run simulations and get stats.
"""
import logging
import sys

import sim
import stats

log = logging.getLogger()


def play_simple_game():
    playedGame = sim.play_game()
    log.info("And the winner is %s", playedGame.winner.name)


def get_function_from_name(name):
    if not name:
        log.setLevel(level=logging.DEBUG)
        return play_simple_game

    return getattr(stats, name)


if __name__ == '__main__':
    fmt = '%(name)s:%(funcName)s:%(lineno)s %(levelname)s: %(message)s'
    logging.basicConfig(format=fmt)
    func = get_function_from_name(None if len(sys.argv) == 1 else sys.argv[1])
    log.info("%s() ...", func.__name__)
    func()
