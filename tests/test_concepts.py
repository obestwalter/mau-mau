import pytest

from mau_mau import exceptions
from mau_mau.concepts import _CardCollection


@pytest.mark.parametrize(
    "data, expectation",
    [
        ([], False),
        ([None], True),
        ([1], True),
        (["hello", 3], True),
        ([1, 2, 3], True),
    ],
)
def test_len_and_bool_depending_on_len(data, expectation):
    assert len(_CardCollection(data)) == len(data)
    assert bool(_CardCollection(data)) == expectation


@pytest.mark.parametrize("data", [[], [None], [1], ["hello", 3], [1, 2, 3]])
def test_iter(data):
    assert [e for e in _CardCollection(data)] == data


@pytest.mark.parametrize(
    "data, wantedItem, expectation",
    [
        (["a", "b"], 1, "a"),
        (["c", "d", "e", "f"], 1, "c"),
        (["e", "f"], "f", "f"),
        (["g", "h", "i"], "g", "g"),
        (["m", "n"], None, "m"),
        (["j", "k", "l"], "x", exceptions.CardNotFound),
        (None, 1, exceptions.NoCardsLeft),
        ([], 1, exceptions.NoCardsLeft),
        ([], "a", exceptions.NoCardsLeft),
    ],
)
def test_fetch(data, wantedItem, expectation):
    c = _CardCollection(data)
    if isinstance(expectation, str):
        assert c.fetch(wantedItem) == expectation
    else:
        with pytest.raises(expectation):
            c.fetch(wantedItem)
