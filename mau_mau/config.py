import mau_mau.cardroom as mc


class DECK:
    SEVEN = 7
    EIGHT = 8
    JACK = 'Jack'
    VALUES = [SEVEN, EIGHT, 9, 10, JACK, 'Queen', 'King', 'Ace']
    SUITS = ['♦', '♥', '♠', '♣']

    def __init__(self):
        self.len = len(self.make_initializers())

    @classmethod
    def make_initializers(cls):
        return [(v, s) for v in cls.VALUES for s in cls.SUITS]

    @classmethod
    def create(cls):
        return [mc.Card(*i) for i in cls.make_initializers()]

    def __len__(self):
        return self.len
