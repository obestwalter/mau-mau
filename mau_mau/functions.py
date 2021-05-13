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


def put(player, table, card, strategy):
    log.debug(f"play {card}")
    card = player.hand.fetch(card)
    table.waste.put(table.upcard)
    table.upcard = card
    oldRule = table.rule
    table.rule = table.rules.get_rule(card)
    table.rule.strategy = strategy
    table.transfer_punishments(oldRule, table.rule)
