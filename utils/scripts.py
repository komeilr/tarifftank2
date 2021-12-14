import csv

from config.settings import BASE_DIR


def get_table(tablename):
    import tarifftank.models as models
    table = vars(models)[tablename]
    return table


def csv_to_table(filename="TPHS.csv", tablename='CA2021'):
    with open(BASE_DIR / f"tarifftank/data/csv/{filename}", 'r') as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        data = []
        for row in reader:
            data.append(row)
    
    table = get_table(tablename)
    fields = data[0][:33]
    print(fields)
    for row in data[1:]:
        row_dict = {k.lower():v for k, v in zip(fields, row)}
        table.objects.create(**row_dict)
        
