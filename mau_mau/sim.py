import logging

from mau_mau import cardroom

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


# TODO add way to assign different strategies to players
def invite_players(players):
    """Create a sequence of player objects from an amount or some names.

    :type players: int or list of str
    """
    try:
        players = [cardroom.Player(name) for name in players]
    except TypeError:
        players = [cardroom.Player("Player %s" % (n))
                   for n in range(1, players + 1)]
    log.debug("invited players are: %s", players)
    return players


def sit_down_players(players):
    """Players sit down so they know who comes next"""
    for idx, player in enumerate(players):
        try:
            player.nextPlayer = players[idx + 1]
        except IndexError:
            player.nextPlayer = players[0]
