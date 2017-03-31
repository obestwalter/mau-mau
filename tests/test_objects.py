import pytest

from mau_mau import exceptions
from mau_mau.objects import Stock, Waste, Card


def test_fetch_card_from_empty_stock_raises():
    with pytest.raises(exceptions.NoCardsLeft):
        Stock().fetch()


def test_empty_stock():
    assert not Stock()


def test_non_empty_stock():
    assert Stock([0])


def test_fetch_card_from_stock_returns_and_removes_it():
    card = Card(None, None)
    stock = Stock(card)
    assert stock.fetch() == card
    assert not stock


def test_waste_put_adds_card():
    waste = Waste()
    assert not waste.cards
    waste.put(1)
    assert len(waste.cards) == 1
    waste.put(1)
    assert len(waste.cards) == 2
