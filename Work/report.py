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
        for rowno, row in enumerate(rows):
            holding = dict(zip(headers, row))
            try:
                portfolio.append(holding)
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
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
    ''' counts if we made a profit if we sell now '''
    portfolio = read_portfolio(portfolio_data)
    prices = read_prices(prices_data)
    part_sum = 0.0
    for i in portfolio:
        part_sum += float(i['shares'])*(float(prices[i['name']])- i['price'])
        return(print(part_sum))

def make_report(portfolio, prices):
    ''' makes a list of tuples '''
    report = []
    for i in portfolio:
        holding = (i['name'], int(i['shares']), float(prices[i['name']]), (float(prices[i['name']])- float(i['price'])))
        report.append(holding)
    return report

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(((('-'*10) + ' ') *3)+ ('-' * 10))
    for r in report:
        print(f'{r[0]:>10s}{r[1]:>10d}{("$"+str(round(r[2],2))):>12s}{r[3]:>11.2f}')


portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
print_report(report)


