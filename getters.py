# from parse import *
from constants import *


def get_inflation(price_0, price_1):
    """Takes an initial price and a final price as parameters.
    Returns the rate of inflation in percentage
    """
    return 100 * (price_1 - price_0) / price_0


def get_prod_price(period, prod_id, prices):
    """Takes a period, a product id (int) and the list of prices (dic) as parameters.
    Returns a dictionary with the price of that product on that period for all supermarkets.
    (supermarket id (int) as keys, prices (float) as values)
    """
    if period not in prices.keys():
        raise ValueError('período no encontrado.')
    if prod_id not in prices[period][1].keys():
        raise ValueError('producto no encontrado')
    return prices[period][1][prod_id]


def get_prod_inflation(start, end, prod_id, sup_id, prices):
    """
    """
    try:
        price_0 = get_prod_price(start, prod_id, prices)[sup_id]
        price_1 = get_prod_price(end, prod_id, prices)[sup_id]
    except KeyError:
        raise ValueError('supermercado no encontrado.')
    if start >= end:
        raise ValueError('el fin tiene que ser luego del inicio.')
    return get_inflation(price_0, price_1)


def get_sup_inflation(start, end, sup_id, products, prices):
    """Takes a period (starting and ending, ints), a supermarket id (int), the list of prices and products (dic) as parameters. Returns the average inflation for that period and that supermarket.
    """
    acum = 0
    for i in products.keys():
        acum += get_prod_inflation(start, end, i, sup_id, prices)
    return acum / len(products.keys())


def get_best_price(period, prod_id, prices):
    """
    """
    dic = prices[period][1][prod_id]
    min_val = min(dic.values())
    supers = [key for key in dic if dic[key] == min_val]
    return min_val, supers


def get_average_inflation(start, end, products, prices, supers):
    result = int()
    for sup_id in supers:
        result += get_sup_inflation(start, end, sup_id, products, prices)
    return result / len(supers)
