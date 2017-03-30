#!/usr/bin/env python3
"""
This module gives simple command line access to the functions.

Start it without parameters to run a simple game.

Start it with one of the functions in stat.py to run simulations and get stats.
"""
import logging
import sys

from mau_mau import rules, play, stats

try:
    import win_unicode_console
    win_unicode_console.enable()
except ImportError:
    win_unicode_console = None


log = logging.getLogger()
_rulesOfTheGame = rules.MauMau()


def play_simple_game(players=3):
    log.setLevel(level=logging.DEBUG)
    finishedGame = play.play_game(_rulesOfTheGame, players)
    log.info("And the winner is %s", finishedGame.table.winner.name)


def play_interactive_game():
    log.setLevel(level=logging.DEBUG)
    playedGame = play.play_game(_rulesOfTheGame, ['Eric', 'John', 'human'])
    log.info("And the winner is %s", playedGame.table.winner.name)


def get_function_from_name(name):
    if not name:
        return play_simple_game

    try:
        return getattr(stats, name)

    except AttributeError:
        return play_interactive_game


def simple_parse_args(argv):
    """For more sophisticated stuff use argparse, fire, plumbum, click, ..."""
    return (None if len(argv) == 1 else argv[1],
            argv[2:] if len(argv) > 2 else [])


def main():
    try:
        fmt = '%(name)-20s%(lineno)-3s %(funcName)-17s: %(message)s'.format()
        logging.basicConfig(format=fmt, level=logging.INFO)
        functionName, args = simple_parse_args(sys.argv)
        function = get_function_from_name(functionName)
        log.info("%s(%s) ...", function.__name__, ", ".join(args))
        function(*args)

    except KeyboardInterrupt:
        log.error("\nfatal: lost game by chickening out!")
        return 1


if __name__ == '__main__':
    sys.exit(main())
