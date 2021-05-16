import logging
from collections import Iterable

from mau_mau import rules, objects
from mau_mau.constants import DECK
from mau_mau.functions import draw
from mau_mau.objects import Stock, Waste
from mau_mau.strategies import BasicStrategy
from mau_mau.subjects import Player

log = logging.getLogger(__name__)


def play_game(gameRules, playerSeed):
    deck = [(v, s) for v in DECK.VALUES for s in DECK.SUITS]
    deckLen = len(deck)

    if not isinstance(playerSeed, Iterable):
        players = [Player(f"Player {n}") for n in range(1, playerSeed + 1)]
    else:
        players = [Player(p) for p in playerSeed]

    numPlayers = len(players)
    assert numPlayers > 1, "not enough players (need at least two)"
    neededCards = numPlayers * gameRules.cardsPerPlayer
    assert neededCards <= deckLen, f"too many players ({numPlayers})"

    table = objects.Table()
    table.rules = gameRules
    table.stock = Stock(deck)
    table.stock.shuffle()
    table.waste = Waste()
    table.upcard = table.stock.fetch()
    table.rule = gameRules.get_rule(table.upcard)

    for this_player in players:
        table.stock, table.waste = draw(
            this_player, table.stock, table.waste, gameRules.cardsPerPlayer
        )

    assert table.upcard
    tableCardsLen = len(table.stock) + len(table.waste) + 1
    handsLen = sum(len(p.hand) for p in players if p.hand)
    assert tableCardsLen + handsLen == deckLen, (
        tableCardsLen,
        handsLen,
        deckLen,
    )

    log.debug("Start new game")
    current_player_index = 0
    strategy = BasicStrategy()
    while True:
        log.debug(f"upcard: {table.upcard}")
        if current_player_index >= len(players):
            current_player_index = 0
        player = players[current_player_index]
        log.debug(f"{player} is up")

        strategy.play(table, player)
        try:
            return [p for p in players if len(p.hand) == 0][0]
        except IndexError:
            pass
        current_player_index += 1


if __name__ == "__main__":
    # TODO cannot pass what to play from command line
    # TODO make possible to pass normal play and sim stuff
    logging.basicConfig(
        format="%(name)-20s%(lineno)-3s %(funcName)-17s: %(message)s".format(),
        level=logging.DEBUG
    )
    # playerNames = ["Eric", "John", "human"]
    the_winner = play_game(rules.MauMau(), 3)
    log.info(f"And the winner is {the_winner.name}")
