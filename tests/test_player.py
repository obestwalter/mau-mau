from mau_mau.subjects import Player


def test_player_inequality():
    assert Player("John") != Player("Eric")


def test_player_equality():
    assert Player("Terry") == Player("Terry")


def test_players_with_same_name_can_be_different_objects():
    assert Player("Terry") is not Player("Terry")
