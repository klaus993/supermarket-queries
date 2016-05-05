from constants import *


def get_inflation(price_0, price_1):
    return 100 * (price_1 - price_0) / price_0


def get_prod_price(period, prod_id):
    """
    """
    if period not in PRICES.keys():
        raise ValueError('period not found.')
    if prod_id not in PRICES[period][1].keys():
        raise ValueError('product not found.')
    return PRICES[period][1][prod_id]


def get_product_inflation(start, end, prod_id, sup_id):
    price_0 = get_prod_price(start, prod_id)[sup_id]
    price_1 = get_prod_price(end, prod_id)[sup_id]
    return get_inflation(price_0, price_1)


def get_average_inflation(start, end, sup_id):
    for price in PRICES[start][0][sup_id].values():
        pass
