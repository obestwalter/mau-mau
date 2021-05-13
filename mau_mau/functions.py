import logging

log = logging.getLogger(__name__)


def draw(player, table, amount=1):
    for _ in range(amount):
        if not table.stock:
            table.replenish_stock()
        card = table.stock.fetch()
        player.hand.put(card)
        log.debug(f"{player.name} <- {card}")


def put(player, table, card, strategy):
    log.debug(f"play {card}")
    card = player.hand.fetch(card)
    table.waste.put(table.upcard)
    table.upcard = card
    oldRule = table.rule
    table.rule = table.rules.get_rule(card)
    table.rule.strategy = strategy
    table.transfer_punishments(oldRule, table.rule)
