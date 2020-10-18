# report.py
#
# Exercise 2.4

from pprint import pprint
import csv

def read_portfolio(filename):
    '''Reads portfolio'''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        # for row in rows:
        #     holding = (row[0], int(row[1]), float(row[2]))
        #     portfolio.append(holding)
        for row in rows:
            holding = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(holding)
    return portfolio
 
def read_prices(filename):
    '''Reads prices from csv'''
    prices = {}
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        # headers = next.rows
        for row in rows:
            if row:
                prices[row[0]] = row[1]
    
    return prices

def retirement(portfolio_data, prices_data):
    portfolio = read_portfolio('Work/Data/portfolio.csv')
    prices = read_prices('Work/Data/prices.csv')
    part_sum = 0.0
    for i in portfolio:
        #print('Stock ', i['name'],';purchase price ', i['price'], ';sale price ',prices[i['name']])
        #print('Profit of ', (round(float(i['shares']))*((i['price'])-float(prices[i['name']]))))
        part_sum += float(i['shares'])*(float(prices[i['name']])- i['price'])
        return(print(part_sum))

retirement('Work/Data/portfolio.csv', 'Work/Data/prices.csv')
