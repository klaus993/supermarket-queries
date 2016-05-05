from constants import *
# from time import sleep


def get_inflation(price_0, price_1):
    """Takes an initial price and a final price as parameters.
    Returns the rate of inflation in percentage
    """
    return 100 * (price_1 - price_0) / price_0


def get_prod_price(period, prod_id):
    """Takes a period and a product as parameters (int).
    Returns a dictionary with the price of that product on that period for all supermarkets.
    (supermarket id (int) as keys, prices (float) as values)
    """
    if period not in PRICES.keys():
        raise ValueError('period not found.')
    if prod_id not in PRICES[period][1].keys():
        raise ValueError('product id not found.')
    return PRICES[period][1][prod_id]


def get_product_inflation(start, end, prod_id, sup_id):
    """
    """
    if sup_id not in PRICES[start][0].keys():
        raise ValueError('supermarket id not found.')
    if start >= end:
        raise ValueError('end must be a later date than start.')
    price_0 = get_prod_price(start, prod_id)[sup_id]
    price_1 = get_prod_price(end, prod_id)[sup_id]
    return get_inflation(price_0, price_1)


def get_average_inflation(start, end, sup_id):
    """
    """
    acum = 0
    for i in PRODUCTS.keys():
        acum += get_product_inflation(start, end, i, sup_id)
    return acum / len(PRODUCTS.keys())


def get_best_price(period, prod_id):
    """
    """
    dic = PRICES[period][1][prod_id]
    min_val = min(dic.values())
    result = [key for key in dic if dic[key] == min_val]
    return min_val, result
