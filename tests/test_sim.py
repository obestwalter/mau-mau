import pytest

from mau_mau import rules, play
from mau_mau.const import DECK
from mau_mau.subjects import Croupier

mmRules = rules.MauMau()


def test_game_with_too_many_players_crashes_early():
    deckSize = len([(v, s) for v in DECK.VALUES for s in DECK.SUITS])
    tooManyPlayers = deckSize // mmRules.cardsPerPlayer + 2
    with pytest.raises(AssertionError):
        play.play_game(mmRules, tooManyPlayers)


def test_game_with_one_player_crashes_early():
    with pytest.raises(AssertionError):
        play.play_game(mmRules, 1)


def test_game_with_default_amount_of_players_succeeds():
    play.play_game(mmRules, 3)


def test_invite_players_with_names_invites_right_amount():
    names = ['a', 'b', 'c', 'd']
    players = Croupier._create_real_players(names)
    assert len(players) == len(names)
    assert [p.name for p in players] == names


def test_invite_players_with_number_invites_right_amount():
    for n in range(10):
        assert len(Croupier._create_real_players(n)) == n
