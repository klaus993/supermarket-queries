import csv
from constants import PARSE_ERROR, NOT_FOUND


# row[0] = id_supermercado
# row[1] = id_producto
# row[2] = periodo
# row[3] = precio


def to_dict(file):
    """Takes a csv file and parses it into a
    dictionary. Pre condition: the csv file has
    to have only two fields. Returns the dictionary.
    If the file is not found, catches FileNotFound error, informs the user and exits.
    If the file has not got a number as an id (the first field) catches the error, informs the user and exits.
    """
    try:
        dic = dict()
        with open(file) as f:
            rows = csv.reader(f)
            next(rows)
            for row in rows:
                dic[int(row[0])] = row[1]
        return dic
    except OSError:
        print(NOT_FOUND.format(file))
        exit()
    except (ValueError, IndexError):
        print(PARSE_ERROR.format(file))
        exit()


def get_super(row):
    """Gets a row as a parameter (a list of strings)
    Returns the field that represents the supermarket id as an integer.
    If a ValueError raises, returns the field as a string.
    """
    try:
        return int(row[0])
    except ValueError:
        return row[0]


def get_prod(row):
    """Gets a row as a parameter (a list of strings)
    Returns the field that represents the product id as an integer.
    If a ValueError raises, returns the field as a string.
    """
    try:
        return int(row[1])
    except ValueError:
        return row[1]


def get_period(row):
    """Gets a row as a parameter (a list of strings)
    Returns the field that represents the period as an integer.
    If a ValueError raises, returns the field as a string.
    """
    try:
        return int(row[2])
    except ValueError:
        return row[2]


def get_price(row):
    """Gets a row as a parameter (a list of strings)
    Returns the field that represents the price as a float.
    If a ValueError raises, returns the field as a string.
    """
    try:
        return float(row[3])
    except ValueError:
        return row[3]


def get_reader(file):
    """Gets a csv file with 4 fields.
    Returns a row iterator.
    """
    rows = csv.reader(file)
    next(rows)
    return rows


def create_prices_dict(file):
    """Gets a csv file with 4 fields.
    Returns a dictionary.
    If the file is not found, catches FileNotFound error, informs the user and exits.
    If the file has not got 4 fields in any line, catches the error, informs the user and exits.
    """
    try:
        dic = dict()
        with open(file) as f:
            rows = get_reader(f)
            for row in rows:
                if get_period(row) not in dic.keys():
                    dic[get_period(row)] = [{}, {}]
                if get_super(row) not in dic[get_period(row)][0].keys():
                    dic[get_period(row)][0][get_super(row)] = {}
                if get_prod(row) not in dic[get_period(row)][1].keys():
                    dic[get_period(row)][1][get_prod(row)] = {}
                dic[get_period(row)][0][get_super(row)][get_prod(row)] = get_price(row)
                dic[get_period(row)][1][get_prod(row)][get_super(row)] = get_price(row)
        return dic
    except OSError:
        print(NOT_FOUND.format(file))
        exit()
    except IndexError:
        print(PARSE_ERROR.format(file))
        exit()
