name = input('Enter your name')
age = input('Enter your age')

import csv

header = ['name', 'age']
data = [name, age]

with open('countries.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(data)
