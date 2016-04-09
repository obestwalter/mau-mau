import logging

import collections

from mau_mau import cardroom
from mau_mau.strategy import BasicStrategy, ExternalStrategy

log = logging.getLogger(__name__)


def play_game(rulesOfTheGame, players):
    game = setup_game(rulesOfTheGame, players)
    while not game.over:
        player = game.next_turn()
        player.play_turn(game.table)
    return game


def setup_game(rulesOfTheGame, players):
    players = invite_players(players)
    sit_down_players(players)
    deckOfCards = cardroom.DECK.create()
    table = cardroom.Table(rulesOfTheGame, players)
    table.set(deckOfCards)
    table.deal_fresh_hand()
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
            strategy = ExternalStrategy if player == 'human' else BasicStrategy
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
