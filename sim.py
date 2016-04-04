import logging

from cardroom import Game, Table, Player, Stock, Waste, Card


log = logging.getLogger(__name__)


def play_game(players=3, cardsPerPlayer=5):
    game = start_new_game(players, cardsPerPlayer)
    while not game.over:
        game.next_turn()
        play_turn(game.player, game.table)
    return game


def start_new_game(players, cardsPerPlayer):
    players = invite_players(players)
    deck = fetch_fresh_deck_of_cards()
    ensure_sure_we_are_ok_to_play(players, cardsPerPlayer, deck)
    table = set_the_table(deck)
    for player in players:
        deal_cards(player, table.stock, cardsPerPlayer)
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
    class Def:
        values = [7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        suits = ['diamonds', 'hearts', 'spades', 'clubs']

    deck = Stock([Card(v, s) for v in Def.values for s in Def.suits])
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


def deal_cards(player, stock, cardsPerPlayer):
    deal = stock.fetch_cards(cardsPerPlayer)
    player.hand = deal
    log.debug(str(player))


def play_turn(player, table):
    if not player.play_card(table):
        # FIXME this could be more symmetric to what happens in play_card
        # - draw_card returns boolean
        # - if False (stock empty)
        # - replenish stock
        # - draw again
        ensure_stock_is_replenished(table)
        player.draw_card(table.stock)


def ensure_stock_is_replenished(table):
    if table.stock.isEmpty:
        table.stock = Stock(table.waste.cards)
        table.waste = Waste()
        table.stock.shuffle()
