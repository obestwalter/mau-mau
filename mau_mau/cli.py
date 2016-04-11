#!/usr/bin/env python3
"""
This module gives simple command line access to the functions.

Start it without parameters to run a simple game.

Start it with one of the functions in stat.py to run simulations and get stats.
"""
import logging
import sys

from mau_mau import rules, sim, stats

log = logging.getLogger()
_rulesOfTheGame = rules.MauMau()


def play_simple_game(players=3):
    log.setLevel(level=logging.DEBUG)
    playedGame = sim.play_game(_rulesOfTheGame, players)
    log.info("And the winner is %s", playedGame.table.winner.name)


def play_interactive_game():
    log.setLevel(level=logging.DEBUG)
    playedGame = sim.play_game(_rulesOfTheGame, ['Eric', 'John', 'human'])
    log.info("And the winner is %s", playedGame.table.winner.name)


def get_function_from_name(name):
    if not name:
        return play_simple_game

    try:
        return getattr(stats, name)

    except AttributeError:
        return play_interactive_game


def simple_parse_args(argv):
    """For more sophisticated stuff use argparse or a cli tool like plumbum"""
    return (None if len(argv) == 1 else argv[1],
            argv[2:] if len(argv) > 2 else [])


def main():
    try:
        fmt = '%(name)-20s%(lineno)-3s %(funcName)-17s: %(message)s'.format()
        logging.basicConfig(format=fmt, level=logging.INFO)
        functionName, args = simple_parse_args(sys.argv)
        functionObject = get_function_from_name(functionName)
        log.info("%s(%s) ...", functionObject.__name__, ", ".join(args))
        functionObject(*args)
        return 0
    except KeyboardInterrupt:
        print("\n... bye!")


if __name__ == '__main__':
        sys.exit(main())
