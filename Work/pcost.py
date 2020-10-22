# pcost.py
#
# Exercise 1.27

import sys
import csv

def portfolio_cost(filename):
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    total_cost = 0
    for rowno, row in enumerate(rows, start = 1):
        record = dict(zip(headers, row))
        try:
            nshares = int(record['shares'])
            price = float(record['price'])
            total_cost += nshares * price
            #t = (row[0], int(row[1]), float(row[2]))
            #sum = sum + (t[1] * t[2])
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')
    return(total_cost)
    f.close()

# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = 'Data/portfolio.csv'

# cost = portfolio_cost('Data/portfolio.csv')
cost = portfolio_cost('Data/portfoliodate.csv')
#cost = portfolio_cost('Data/missing.csv')
print('Total cost:', cost)
