# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''

    portfolio = []
    holding = {}

    with open(filename, 'rt') as f:

        rows = csv.reader(f)
        headers = next(rows)

        for row in rows: 
            holding = {
                    'name' : row[0],
                    'shares' : int(row[1]),
                    'prices' : float(row[2])
                    }
            
            portfolio.append(holding)
            
    return portfolio


