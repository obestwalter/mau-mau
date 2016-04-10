import pytest

from mau_mau.objects import Stock, Waste, Card


def test_fetch_card_from_empty_stock_raises():
    with pytest.raises(Stock.StockEmpty):
        Stock().fetch_card()


def test_empty_stock():
    assert Stock().isEmpty


def test_non_empty_stock():
    assert not Stock([0]).isEmpty


def test_fetch_card_from_stock_returns_and_removes_it():
    card = Card(None, None)
    stock = Stock(card)
    assert stock.fetch_card() == card
    assert stock.isEmpty


def test_waste_put_adds_card():
    waste = Waste()
    assert not waste.cards
    waste.put_card(1)
    assert len(waste.cards) == 1
    waste.put_card(1)
    assert len(waste.cards) == 2
