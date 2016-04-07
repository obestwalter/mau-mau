from cardroom import Player


def test_player_has_not_won_immediately_after_creation():
    assert not Player(1).hasWon


def test_player_has_not_won_with_cards():
    player = Player(1)
    player.hand = [1]
    assert not player.hasWon


def player_inequality():
    assert Player('John') != Player('Eric')


def player_equality():
    assert Player('Terry') == Player('Terry')


def test_players_with_same_name_can_be_different_objects():
    assert Player('Terry') is not Player('Terry')
