from constants import *


def get_prod_price(start, end, prod_id):
    """
    """
    if start >= end:
        raise ValueError('end must be greater than start.')
    if start not in PRICES.keys() or end not in PRICES.keys():
        raise ValueError('period not found.')
    if prod_id not in PRICES[start][1].keys():
        raise ValueError('product not found.')
    return PRICES[start][1][prod_id], PRICES[end][1][prod_id]


def get_product_inflation(start, end, prod_id, sup_id):
    price_0 = get_prod_price(start, end, prod_id)[0][sup_id]
    price_1 = get_prod_price(start, end, prod_id)[1][sup_id]
    inflation = 100 * (price_1 - price_0) / price_0
    return inflation

print('{0:.2f}%'.format(get_product_inflation(201504, 201603, 102, 1)))




