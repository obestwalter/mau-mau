import pytest

from sim import simulate_game


def test_simulation_with_too_many_players_crashes_early():
    with pytest.raises(AssertionError):
        simulate_game(7)


def test_simulation_with_decent_amount_of_players_succeeds():
    simulate_game(3)
