import logging

from cardroom import Game, Table, Player, Stock, Waste, Card
from rules import DECK, rule_class

log = logging.getLogger(__name__)


def play_game(players=3, cardsPerPlayer=5):
    game = start_new_game(players, cardsPerPlayer)
    while not game.over:
        game.next_turn()
        game.player.play_turn(game.table)
    return game


def start_new_game(players, cardsPerPlayer):
    players = invite_players(players)
    deck = fetch_fresh_deck_of_cards()
    ensure_sure_we_are_ok_to_play(players, cardsPerPlayer, deck)
    table = set_the_table(deck)
    for player in players:
        player.hand = table.stock.fetch_cards(cardsPerPlayer)
    return Game(players, table)


def invite_players(players):
    """Create a sequence of player objects from an amount or some names.

    :type players: int or list of str
    """
    try:
        players = [Player(name) for name in players]
    except TypeError:
        players = [Player("Player %s" % (n)) for n in range(1, players + 1)]
    log.debug("invited players are: %s", players)
    return players


def fetch_fresh_deck_of_cards():
    """Magic a fresh deck of cards out of nothing from a definition"""
    initializers = [(v, s) for v in DECK.VALUES for s in DECK.SUITS]
    deck = Stock([Card(*i, rule=rule_class(i[0])(*i)) for i in initializers])
    log.debug(str(deck))
    return deck


def ensure_sure_we_are_ok_to_play(players, cardsPerPlayer, deck):
    assert len(players) > 1
    assert len(players) * cardsPerPlayer <= len(deck)


def set_the_table(deck):
    deck.shuffle()
    stock = deck
    upcard = stock.fetch_card()
    waste = Waste()
    return Table(stock, waste, upcard)
