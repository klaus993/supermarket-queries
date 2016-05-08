from getters import *
from constants import START, END


def press_to_continue():
    """Asks input for the user to pass, used for a pause after results are shown.
    """
    input('\nPresiona ENTER para continuar')


def convert_period(period):
    """Converts user entered periods to the corresponding dict keys
    """
    if len(period) != 7 or period[2] != '-':
        raise ValueError('sintaxis incorrecta (MM-AAAA).')
    return period[3:] + period[:2]


def ask_and_convert(prices, string):
    """Asks the user for a starting and an ending period and returns the converted periods as a tuple.
    """
    try:
        period = int(convert_period(input('Ingrese mes y año de {}: '.format(string))))
    except ValueError:
        raise ValueError('período no encontrado.')
    if period not in prices.keys():
        raise ValueError('período no encontrado.')
    return period


def ask_average_inflation(supers, products, prices):
    """Gets three dics as parameters (products, prices and supers).
    Asks the user for a period to print the average inflation rate. If the periods are not in the dict, the function raises an exception.
    """
    enter_loop = True
    while enter_loop:
        try:
            start = ask_and_convert(prices, START)
            end = ask_and_convert(prices, END)
            print ('\nInflación general promedio: {:.2f}%'.format(get_average_inflation(start, end, products, prices, supers)))
            press_to_continue()
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
            start = ask_and_convert(prices, START)
            end = ask_and_convert(prices, END)
            print()
            for sup_id in supers:
                print('{}: {:.2f}%'.format(supers[sup_id], get_sup_inflation(start, end, sup_id, products, prices)))
            press_to_continue()
            enter_loop = False
        except ValueError as e:
            print('Error: ' + str(e))


def ask_prod(products):
    """Asks the user for a product. Suggests products according to the user input.
    Asks the user if the displayed product is correct. If it is, returns the product_id.
    If it's not, returns None.
    """
    string = str()
    while not string:
        string = input('Ingrese el nombre de un producto: ')
    for key in products:
        if string in products[key]:
            loop = True
            while loop:
                is_prod = input('\n [{}]\n¿Es este el producto deseado? [s/n]: '.format(products[key]))
                if is_prod == 's' or is_prod == 'S':
                    return key
                if is_prod != 'n' and is_prod != 'N':
                    print('\nOpción no reconocida. Vuelva a ingresar.')
                else:
                    loop = False


def prod_inflation(supers, products, prices):
    """
    """
    enter_loop = True
    while enter_loop:
        try:
            start = ask_and_convert(prices, START)
            end = ask_and_convert(prices, END)
            prod_id = int()
            while not prod_id:
                prod_id = ask_prod(products)
                if not prod_id:
                    print('Producto no encontrado.')
            print()
            for sup_id in supers:
                print('{}: {:.2f}%'.format(supers[sup_id], get_prod_inflation(start, end, prod_id, sup_id, prices)))
            press_to_continue()
            enter_loop = False
        except ValueError as e:
            print('Error: ' + str(e))


def best_price(supers, products, prices):
    """
    """
    enter_loop = True
    while enter_loop:
        try:
            period = ask_and_convert(prices, 'búsqueda')
            prod_id = ask_prod(products)
            best_price = get_best_price(period, prod_id, prices)
            for sup_id in best_price[1]:
                print('\n{}'.format(supers[sup_id]), end=' ')
            print(': ${}'.format(best_price[0]))
            press_to_continue()
            enter_loop = False
        except ValueError as e:
            print('Error: ' + str(e))


def print_menu(menu):
    """
    """
    print('\nMenú principal')
    print('------')
    for option in menu:
        print('{}. {}'.format(option, menu[option]))
    print('------')


def interactive_menu(supers, products, prices):
    """
    """
    menu = {1: 'Inflación por supermercado',
            2: 'Inflación por producto',
            3: 'Inflación general promedio',
            4: 'Mejor precio para un producto',
            5: 'Salir'
            }
    enter_loop = True
    while enter_loop:
        print_menu(menu)
        try:
            choice = int(input('Opción: '))
        except ValueError:
            print('Debe ingresar un número.')
            press_to_continue()
            continue
        if choice == 1:
            ask_sup_inflation(supers, products, prices)
        elif choice == 2:
            prod_inflation(supers, products, prices)
        elif choice == 3:
            ask_average_inflation(supers, products, prices)
        elif choice == 4:
            best_price(supers, products, prices)
        elif choice == 5:
            enter_loop = False
        elif choice not in menu.keys():
            input('Opción incorrecta, presione ENTER y vuelva a ingresar.')
