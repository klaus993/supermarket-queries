def get_inflation(price_0, price_1):
    """Takes an initial price and a final price as parameters.
    Returns the rate of inflation in percentage
    """
    return 100 * (price_1 - price_0) / price_0


def get_prod_price(period, prod_id, sup_id, prices):
    """Takes a period, a product id (int) and the list of prices (dic) as parameters.
    Returns a dictionary with the price of that product on that period for all supermarkets.
    (supermarket id (int) as keys, prices (float) as values)
    If the period or product does not exist, raises a ValueError.
    """
    if period not in prices.keys():
        raise ValueError('período no encontrado.')
    if prod_id not in prices[period][1].keys():
        raise ValueError('producto no encontrado')
    return prices[period][1][prod_id][sup_id]


def get_prod_inflation(start, end, prod_id, sup_id, prices):
    """Takes a period (starting and ending, ints), a prod id and a sup id (ints) and the list of prices as parameters.
    Returns the given product inflation rate for that period and that supermarket.
    If the dict search raises a KeyError, it catches the error and raises a ValueError.
    If the starting period is a later date than the ending, it raises a ValueError.
    """
    try:
        price_0 = get_prod_price(start, prod_id, sup_id, prices)
        price_1 = get_prod_price(end, prod_id, sup_id, prices)
    except KeyError:
        raise ValueError('supermercado no encontrado.')
    if start >= end:
        raise ValueError('el fin tiene que ser luego del inicio.')
    return get_inflation(price_0, price_1)


def get_sup_inflation(start, end, sup_id, products, prices):
    """Takes a period (starting and ending, ints), a supermarket id (int), the list of prices and products (dic) as parameters.
    Returns the average inflation for that period and that supermarket.
    """
    acum = int()
    for prod_id in products:
        acum += get_prod_inflation(start, end, prod_id, sup_id, prices)
    return acum / len(products.keys())


def get_best_price(period, prod_id, prices):
    """Takes a period (int), a prod id (int) and the list of prices (dict) as parameters.
    Returns a tuple containing the best price value (float) in the [0] position, and a list
    of super ids (int) containing the supermarkets that offer that value in that period.
    """
    dic = prices[period][1][prod_id]
    min_val = min(dic.values())
    supers = [key for key in dic if dic[key] == min_val]
    return min_val, supers


def get_average_inflation(start, end, products, prices, supers):
    """Takes periods start, end (ints), and three dicts (products, prices and supers)
    Returns the general average inflation rate (percentage) (float).
    """
    result = int()
    for sup_id in supers:
        result += get_sup_inflation(start, end, sup_id, products, prices)
    return result / len(supers)
