import csv
from time import sleep

def parse_to_dict(file):
    """Takes a csv file and parses it into a
    dictionary. Pre condition: the csv file has
    to have only two fields. Returns the dictionary.
    """
    dic = {}
    with open(file) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            dic[row[0]] = row[1]
    return dic


def prices_to_dict(file, supermarket_id, product_id):
    dic = {}
    with open(file) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            if row[0] == supermarket_id and row[1] == product_id:
                print(row)
                sleep(0.1)
                dic[row[2]] = row[3]
    return dic
