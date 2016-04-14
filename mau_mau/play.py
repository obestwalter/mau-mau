import logging

from mau_mau import concepts, subjects, objects

log = logging.getLogger(__name__)


def play_game(gameRules, playerSeed):
    game = setup_game(gameRules, playerSeed)
    while not game.over:
        player = game.next_turn()
        player.play(game.table)
    return game


def setup_game(rules, playerSeed):
    croupier = subjects.Croupier()
    table = objects.Table()

    croupier.fetch_fresh_deck_of_cards()
    croupier.invite(playerSeed, table)
    croupier.check_setup(table.players, rules.cardsPerPlayer)
    croupier.set_table(table, rules)
    for player in table.players:
        player.draw(table, rules.cardsPerPlayer)
    croupier.check_table(table)
    game = concepts.Game(table)
    log.debug("Start new game: %s", game)
    return game
