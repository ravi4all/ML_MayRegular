import csv

data = [
    {"name":'Ram',"email":'ram@gmail.com','pwd':'1234'},
    {"name":'Ram',"email":'ram@gmail.com','pwd':'1234'},
    {"name":'Ram',"email":'ram@gmail.com','pwd':'1234'},
    {"name":'Ram',"email":'ram@gmail.com','pwd':'1234'}
]

with open('data_2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row.values())