from ui import *


def main():
    """
    """
    SUPERS = to_dict('supermercados.csv')
    PRODUCTS = to_dict('productos.csv')
    PRICES = create_prices_dict('precios.csv')
    interactive_menu(SUPERS, PRODUCTS, PRICES)


main()
