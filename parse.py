import csv
from time import sleep


CSV_ERROR = 'El csv debe tener {} campos.'
# row[0] = id_supermercado
# row[1] = id_producto
# row[2] = periodo
# row[3] = precio


def parse_to_dict(file):
    """Takes a csv file and parses it into a
    dictionary. Pre condition: the csv file has
    to have only two fields. Returns the dictionary.
    """
    dic = dict()
    n = 2
    with open(file) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            if len(row) != n:
                raise TypeError(CSV_ERROR.format(n))
            dic[row[0]] = row[1]
    return dic


def prices_to_dict(file):
    dic = dict()
    n = 4
    with open(file) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            if len(row) != n:
                raise TypeError(CSV_ERROR.format(n))
            dic[row[2]] = {row[0]: {row[1]: row[3]}}
    return dic


def get_super(row):
    return int(row[0])


def get_prod(row):
    return int(row[1])


def get_period(row):
    return int(row[2])


def get_price(row):
    return float(row[3])


def initialize_reader(file):
    rows = csv.reader(file)
    next(rows)
    return rows


def initialize_prices_dict(file):
    with open(file) as f:
        dic = {}
        rows = initialize_reader(f)
        for row in rows:
            if get_period(row) in dic.keys():
                break
            dic[get_period(row)] = [{}, {}]
        f.seek(0)
        next(rows)
        for i in range(1, 4):
            for row in rows:
                dic[get_period(row)][0][i] = {}
            f.seek(0)
            next(rows)
        for i in range(1, 20737):
            for row in rows:
                dic[get_period(row)][1][i] = {}
            f.seek(0)
            next(rows)
    return dic


def insert_prices(file):
    dic = initialize_prices_dict(file)
    with open(file) as f:
        rows = initialize_reader(f)
        for row in rows:
            dic[get_period(row)][0][get_super(row)][get_prod(row)] = get_price(row)
        for row in rows:
            dic[get_period(row)][1][get_prod(row)][get_super(row)] = get_price(row)
    return dic

