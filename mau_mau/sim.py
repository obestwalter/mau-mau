import logging

import collections

from mau_mau import cardroom
from mau_mau.config import DECK
from mau_mau.strategy import BasicStrategy, HumanStrategy
from mau_mau.subjects import Croupier

log = logging.getLogger(__name__)


def play_game(rulesOfTheGame, players):
    game = setup_game(rulesOfTheGame, players)
    while not game.over:
        player = game.next_turn()
        player.play_turn(game.table)
    return game


def setup_game(rules, players):
    croupier = Croupier()
    players = invite_players(players)
    croupier.ensure_setup_ok(players, rules.cardsPerPlayer)
    sit_down_players(players)
    deckOfCards = DECK.create()
    table = cardroom.Table(rules, players)
    table.set(deckOfCards)
    for player in table.players:
        croupier.deal_fresh_hand(player, table.stock, rules.cardsPerPlayer)
    game = cardroom.Game(table)
    log.debug("Start new game: %s", game)
    return game


def invite_players(players):
    """Create a sequence of player objects from an amount or some names.

    :type players: int or list of str
    """
    invitedPlayers = []
    if isinstance(players, collections.Iterable):
        for player in players:
            strategy = HumanStrategy if player == 'human' else BasicStrategy
            invitedPlayers.append(cardroom.Player(player, strategy))
    else:
        invitedPlayers = [cardroom.Player("Player %s" % (n))
                          for n in range(1, players + 1)]
    log.debug("invited players are: %s", invitedPlayers)
    return invitedPlayers


def sit_down_players(players):
    """Players sit down so they know who comes next"""
    for idx, player in enumerate(players):
        try:
            player.nextPlayer = players[idx + 1]
        except IndexError:
            player.nextPlayer = players[0]
