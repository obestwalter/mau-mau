import logging

from mau_mau.objects import Waste

log = logging.getLogger(__name__)


def draw(player, stock, waste, amount=1):
    for _ in range(amount):
        if not stock:
            stock = waste
            stock.shuffle()
            waste = Waste()
        card = stock.fetch()
        player.hand.put(card)
        log.debug(f"{player.name} <- {card}")
    return stock, waste
