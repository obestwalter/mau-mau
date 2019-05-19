import logging
import sys

import fire

from mau_mau import constants, concepts, subjects, rules, objects

log = logging.getLogger(__name__)


def play_game(gameRules, playerSeed):
    game = setup_game(gameRules, playerSeed)
    while not game.over:
        player = game.next_turn()
        player.play(game.table)
    return game


def setup_game(rules, playerSeed):
    croupier = subjects.Croupier()
    croupier.fetch_fresh_deck_of_cards()
    table = objects.Table()
    croupier.invite(playerSeed, table)
    croupier.check_setup(table.players, rules.cardsPerPlayer)
    croupier.set_table(table, rules)
    for player in table.players:
        player.draw(table, rules.cardsPerPlayer)
    croupier.check_table(table)
    game = concepts.Game(table)
    log.debug("Start new game: %s", game)
    return game


def cli():
    """Command line interface."""

    class Cli:
        def sim(self, players=3):
            """Simulate a game."""
            self._play(players)

        def play(self, players=["Eric", "John", "human"]):
            """Play a game against two computer players.

            If one of the players' names is 'human' it will be interactive.
            """
            self._play(players)

        @staticmethod
        def _play(players):
            game = play_game(rules.MauMau(), players)
            assert game.over, game
            log.info(f"And the winner is {game.table.winner.name}")

    logging.basicConfig(format=constants.LOG.FMT, level=logging.DEBUG)
    try:
        fire.Fire(Cli)
    except KeyboardInterrupt:
        log.error("\nfatal: lost game by chickening out!")
        sys.exit(1)
