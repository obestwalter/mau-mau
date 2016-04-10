import pytest

from mau_mau import rules, sim
from mau_mau.config import DECK

mmRules = rules.MauMau()


def test_game_with_too_many_players_crashes_early():
    tooManyPlayers = len(DECK()) // mmRules.cardsPerPlayer + 2
    with pytest.raises(AssertionError):
        sim.play_game(mmRules, tooManyPlayers)


def test_game_with_one_player_crashes_early():
    with pytest.raises(AssertionError):
        sim.play_game(mmRules, 1)


def test_game_with_default_amount_of_players_succeeds():
    sim.play_game(mmRules, 3)


def test_invite_players_with_names_invites_right_amount():
    names = ['a', 'b', 'c', 'd']
    players = sim.invite_players(names)
    assert len(players) == len(names)
    assert [p.name for p in players] == names


def test_invite_players_with_number_invites_right_amount():
    for n in range(10):
        assert len(sim.invite_players(n)) == n
