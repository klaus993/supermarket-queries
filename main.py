from ui import *
from time import sleep
from parse import *


def main():
    """Main flux of the program. First, it parses the three data files into dicts.
    The interactive menu function is invoked and it manages the flux of the game, except
    a KeyboardInterrupt (ctrl-c) or EOFError (ctrl-v) are raised. In this case the program
    goes back to the main menu, invoking again the function.
    """
    SUPERS = to_dict('supermercados.csv')
    PRODUCTS = to_dict('productos.csv')
    PRICES = create_prices_dict('precios.csv')
    loop = True
    while loop:
        try:
            interactive_menu(SUPERS, PRODUCTS, PRICES)
            loop = False
        except (KeyboardInterrupt, EOFError):
            try:
                print('\n\nVolviendo al menú principal...')
                sleep(0.4)
            except (KeyboardInterrupt, EOFError):  # In case any of this exceptions is raised during the 0.4 sleep
                continue


main()
