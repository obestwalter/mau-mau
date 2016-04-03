import logging

from model import Game, Table, Player, Stock, Waste, Card


log = logging.getLogger(__name__)


def simulate_game(players=3, cardsPerPlayer=6):
    game = start_new_game(players, cardsPerPlayer)
    while not game.over:
        game.next_turn()
        play_turn(game.player, game.table)
    return game


def start_new_game(players, cardsPerPlayer):
    players = invite_players(players)
    deck = fetch_fresh_deck_of_cards()
    assert len(players) * cardsPerPlayer <= len(deck)
    deck.shuffle()
    stock = deck
    upcard = stock.fetch_card()
    waste = Waste()
    deal_cards(stock, players, cardsPerPlayer)
    return Game(players, Table(stock, waste, upcard))


def play_turn(player, table):
    log.debug("upcard: %s; hand: %s", table.upcard, player.hand)
    playableCard = player.play_card(table.upcard)
    if playableCard:
        table.waste.put_card(table.upcard)
        table.upcard = playableCard
        log.debug("played %s", playableCard)
    else:
        if table.stock.isEmpty:
            table.stock = Stock(table.waste.cards)
            table.waste = Waste()
            table.stock.shuffle()
        player.draw_card(table.stock)


def invite_players(players):
    """Invite players to the game. Can be list of names or amount"""
    try:
        players = [Player(name) for name in players]
    except TypeError:
        players = [Player("Player %s" % (num)) for num in range(1, players)]
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


def deal_cards(stock, players, cardsPerPlayer):
    for player in players:
        deal = stock.fetch_cards(cardsPerPlayer)
        player.hand = deal
        log.debug(str(player))
