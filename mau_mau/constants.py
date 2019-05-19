class DECK:
    SEVEN = 7
    EIGHT = 8
    JACK = "Jack"
    VALUES = [SEVEN, EIGHT, 9, 10, JACK, "Queen", "King", "Ace"]
    SUITS = ["♦", "♥", "♠", "♣"]


class LOG:
    FMT = "%(name)-20s%(lineno)-3s %(funcName)-17s: %(message)s".format()
