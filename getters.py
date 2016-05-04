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
