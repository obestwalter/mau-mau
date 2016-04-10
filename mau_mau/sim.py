import logging

from mau_mau import cardroom
from mau_mau.subjects import Croupier

log = logging.getLogger(__name__)


def play_game(rulesOfTheGame, players):
    game = setup_game(rulesOfTheGame, players)
    while not game.over:
        player = game.next_turn()
        player.play_turn(game.table)
    return game


def setup_game(rules, playerSeed):
    croupier = Croupier()
    croupier.fetch_fresh_deck_of_cards()
    table = cardroom.Table()
    croupier.invite(playerSeed, table)
    croupier.check_setup(table.players, rules.cardsPerPlayer)
    croupier.set_table(table, rules)
    for player in table.players:
        croupier.deal_fresh_hand(player, table.stock, rules.cardsPerPlayer)
    croupier.check_table(table)
    game = cardroom.Game(table)
    log.debug("Start new game: %s", game)
    return game
