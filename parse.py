import csv


def parse_to_dict(file):
    dic = {}
    with open(file) as f:
        csv_super = csv.reader(f)
        next(csv_super)
        for fila in csv.reader(f):
            dic[fila[0]] = fila[1]
    return dic
