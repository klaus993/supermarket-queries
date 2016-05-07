from getters import *


def convert_period(period):
    """
    """
    return int(period[3:] + period[:2])


def ask_convert_start():
    """
    """
    start = input('Ingrese mes y año de inicio: ')
    return convert_period(start)


def ask_convert_end():
    """
    """
    end = input('Ingrese mes y año de fin: ')
    return convert_period(end)


def ask_average_inflation(products, prices, supers):
    start = ask_convert_start()
    end = ask_convert_end()
    print ('Inflación general promedio: {}'.format(get_average_inflation(start, end, products, prices, supers)))

def ask_sup_inflation(supers, products, prices):
    """
    """
    start = ask_convert_start()
    end = ask_convert_end()
    for sup_id in supers:
        print('{}: {:.2f}%'.format(supers[sup_id], get_sup_inflation(start, end, sup_id, products, prices)))


# def ask_prod_inflation(supers, products, prices):
#     """
#     """
#     start = ask_convert_start()
#     end = ask_convert_end()
