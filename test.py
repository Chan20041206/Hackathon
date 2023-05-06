import csv

with open('재료목록full.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = {
        'almond_meal': [],
        'almond': [],
    }
    for row in reader:
        data['almond_meal'].append(row[0])
        data['almond'].append(row[1])

print(data['almond_meal'], '\n')
print(data['almond'])
