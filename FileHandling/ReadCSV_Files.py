import csv
import pandas

with open('data.csv') as file:
    data = csv.reader(file)
    for row in data:
        print(row)
        

df = pandas.read_csv('data.csv')
print(df)
