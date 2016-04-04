import pytest

from sim import play_game, invite_players


def test_game_with_too_many_players_crashes_early():
    with pytest.raises(AssertionError):
        play_game(7)


def test_invite_players_with_names_invites_right_amount():
    names = ['a', 'b', 'c', 'd']
    players = invite_players(names)
    assert len(players) == len(names)
    assert [p.name for p in players] == names


def test_invite_players_with_number_invites_right_amount():
    for n in range(10):
        assert len(invite_players(n)) == n


def test_game_with_one_player_crashes_early():
    with pytest.raises(AssertionError):
        play_game(1)


def test_game_with_default_amount_of_players_succeeds():
    play_game()
