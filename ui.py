from getters import *


def convert_period(period):
    """Converts user 
    """
    return int(period[3:] + period[:2])


def ask_and_convert():
    """Asks the user for a starting and an ending period and returns the converted periods as a tuple.
    """
    start = input('Ingrese mes y año de inicio: ')
    end = input('Ingrese mes y año de fin: ')
    return convert_period(start), convert_period(end)


def ask_convert_end():
    """
    """
    end = input('Ingrese mes y año de fin: ')
    return convert_period(end)


def ask_average_inflation(products, prices, supers):
    start, end = ask_and_convert()
    print ('Inflación general promedio: {:.2f}%'.format(get_average_inflation(start, end, products, prices, supers)))


def ask_sup_inflation(supers, products, prices):
    """
    """
    start, end = ask_and_convert()
    for sup_id in supers:
        print('{}: {:.2f}%'.format(supers[sup_id], get_sup_inflation(start, end, sup_id, products, prices)))


# def ask_prod_inflation(supers, products, prices):
#     """
#     """
#     start = ask_convert_start()
#     end = ask_convert_end()
