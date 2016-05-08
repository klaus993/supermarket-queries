from ui import *
from time import sleep


def main():
    """
    """
    try:
        SUPERS = to_dict('supermercados.csv')
        PRODUCTS = to_dict('productos.csv')
        PRICES = create_prices_dict('precios.csv')
    except TypeError as e:
        print(str(e))
        exit()
    while True:
        try:
            interactive_menu(SUPERS, PRODUCTS, PRICES)
            break
        except (KeyboardInterrupt, EOFError):
            try:
                print('\n\nVolviendo al menú principal...')
                sleep(0.6)
            except (KeyboardInterrupt, EOFError):
                continue


main()
