import csv
import json


def converter(csv_file, json_file, model):
    result = []
    with open(csv_file, encoding='utf-8') as file:
        for row in csv.DictReader(file):
            if 'is_published' in row:
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False
            result.append({'model': model, 'fields': row})

    with open(json_file, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(result))

if __name__ == '__main__':

    converter('ads.csv', 'ads.json', 'avito.ad')
    converter('categories.csv', 'categories.json', 'avito.category')