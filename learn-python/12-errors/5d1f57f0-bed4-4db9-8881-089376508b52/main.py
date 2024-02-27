def purchase(price, money_available):
    if money_available < price:
        raise Exception("not enough money")
    else:
        return money_available - price
