# pcost.py
#
# Exercise 1.27

import sys
import csv

def portfolio_cost(filename):
    f = open('Data/portfolio.csv')
    rows = csv.reader(f)
    headers = next(rows)
    sum = 0

    for row in rows:
        t = (row[0], int(row[1]), float(row[2]))
        sum = sum + (t[1] * t[2])

    return(sum)
    f.close()

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)