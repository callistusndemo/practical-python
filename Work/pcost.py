
import csv

def portfolio_cost(filename):
    ''' Computes total cost of a portfolio value'''
    total = 0.0


    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total += nshares * price 

        return total 
