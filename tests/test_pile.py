import pytest

from model import Stock, Card, _Pile


def test_fetch_card_from_empty_stock_raises():
    with pytest.raises(Stock.StockEmpty):
        Stock().fetch_card()


def test_empty_pile():
    assert _Pile().isEmpty


def test_non_empty_pile():
    assert not _Pile([1]).isEmpty


def test_fetch_card_from_stock_returns_and_removes_it():
    card = Card(None, None)
    stock = Stock(card)
    assert stock.fetch_card() == card
    assert stock.isEmpty
