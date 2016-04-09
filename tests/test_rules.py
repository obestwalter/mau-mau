from mau_mau.rules import MauMau


def test_no_hand_is_not_a_winner_hand():
    assert not MauMau.wins(None)


def test_non_empty_hand_is_not_a_winner_hand():
    assert not MauMau.wins([1])
    assert not MauMau.wins([1, 2])


def test_empty_hand_is_a_winner_hand():
    assert MauMau.wins([])
