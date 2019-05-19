import logging
import sys

import fire

from mau_mau import rules, play
from mau_mau.constants import LOG

try:
    import win_unicode_console

    win_unicode_console.enable()
except ImportError:
    win_unicode_console = None

log = logging.getLogger()


class Cli:
    def __init__(self):
        self.rules = rules.MauMau()

    def sim(self, players=3):
        """simulate a game"""
        log.setLevel(level=logging.DEBUG)
        finishedGame = play.play_game(self.rules, players)
        log.info("And the winner is %s", finishedGame.table.winner.name)

    def play(self):
        """play a game"""
        log.setLevel(level=logging.DEBUG)
        playedGame = play.play_game(self.rules, ["Eric", "John", "human"])
        log.info("And the winner is %s", playedGame.table.winner.name)


def main():
    logging.basicConfig(format=LOG.FMT, level=logging.INFO)
    try:
        fire.Fire(Cli)
    except KeyboardInterrupt:
        log.error("\nfatal: lost game by chickening out!")
        sys.exit(1)
