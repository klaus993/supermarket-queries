from getters import *


def convert_period(period):
    """Converts user entered periods to the corresponding dict keys
    """
    if len(period) != 7 or period[2] != '-':
        raise ValueError('sintaxis incorrecta.')
    return period[3:] + period[:2]


def ask_and_convert(prices):
    """Asks the user for a starting and an ending period and returns the converted periods as a tuple.
    """
    start = int(convert_period(input('Ingrese mes y año de inicio: ')))
    end = int(convert_period(input('Ingrese mes y año de fin: ')))
    if start not in prices.keys() or end not in prices.keys():
        raise ValueError('período no encontrado.')
    return start, end


def ask_and_catch(prices):
    """
    """
    while True:
        try:
            return ask_and_convert(prices)
        except ValueError as e:
            print('Error: ' + str(e))


def ask_average_inflation(products, prices, supers):
    """Gets three dics as parameters (products, prices and supers).
    Asks the user for a period to print the average inflation rate. If the periods are not in the dict, the function raises an exception.
    """
    enter_loop = True
    while enter_loop:
        try:
            start, end = ask_and_convert(prices)
            print ('Inflación general promedio: {:.2f}%'.format(get_average_inflation(start, end, products, prices, supers)))
            enter_loop = False
        except ValueError as e:
            print('Error: ' + str(e))


def ask_sup_inflation(supers, products, prices):
    """Gets three dics as parameters (products, prices and supers).
    Asks the user for a period to print all the supermarket's inflation rate in three different lines.
    """
    enter_loop = True
    while enter_loop:
        try:
            start, end = ask_and_convert(prices)
            for sup_id in supers:
                print('{}: {:.2f}%'.format(supers[sup_id], get_sup_inflation(start, end, sup_id, products, prices)))
                enter_loop = False
        except ValueError as e:
            print('Error: ' + str(e))


# def ask_prod_inflation(supers, products, prices):
#     """
#     """
#     start = ask_convert_start()
#     end = ask_convert_end()
