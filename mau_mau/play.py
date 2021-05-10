import logging
from collections import Iterable

from mau_mau import constants, concepts, subjects, rules, objects
from mau_mau.constants import DECK
from mau_mau.objects import Card, Stock, Waste
from mau_mau.strategies import HumanStrategy, BasicStrategy
from mau_mau.subjects import Player

log = logging.getLogger(__name__)


def play_game(gameRules, playerSeed):
    deck = [Card(v, s) for v in DECK.VALUES for s in DECK.SUITS]
    deckLen = len(deck)

    if not isinstance(playerSeed, Iterable):
        players = [Player(f"Player {n}") for n in range(1, playerSeed + 1)]
    else:
        players = [
            Player(p, HumanStrategy if p == "human" else BasicStrategy)
            for p in playerSeed
        ]

    table = objects.Table()
    table.join(players)

    numPlayers = len(players)
    assert numPlayers > 1, "not enough players (need at least two)"
    neededCards = numPlayers * gameRules.cardsPerPlayer
    assert neededCards <= deckLen, f"too many players ({numPlayers})"

    table.rules = gameRules
    table.stock = Stock(deck)
    table.stock.shuffle()
    table.waste = Waste()
    table.upcard = table.stock.fetch()
    table.rule = gameRules.get_rule(table.upcard)

    for player1 in table.players:
        player1.draw(table, gameRules.cardsPerPlayer)

    assert table.upcard
    tableCardsLen = len(table.stock) + len(table.waste) + 1
    handsLen = sum(len(p.hand) for p in table.players if p.hand)
    assert tableCardsLen + handsLen == deckLen, (
        tableCardsLen,
        handsLen,
        deckLen,
    )

    game1 = concepts.Game(table)
    log.debug("Start new game: %s", game1)
    game = game1
    while not game.over:
        player = game.next_turn()
        player.play(game.table)
    return game


if __name__ == "__main__":
    # TODO cannot pass what to play from command line
    # TODO make possible to pass normal play and sim stuff
    logging.basicConfig(format=constants.LOG.FMT, level=logging.DEBUG)
    # playerNames = ["Eric", "John", "human"]
    numPlayers = 3
    the_game = play_game(rules.MauMau(), numPlayers)
    assert the_game.over, the_game
    log.info(f"And the winner is {the_game.table.winner.name}")
