# report.py
#
# Exercise 2.4

import csv
import sys
import os

if len(sys.argv) != 3:
    print("Usage:", sys.argv[0], "<portfolio list> <price list>")
    os._exit(0)

portfolio = []
prices = {}
profit = {}

def read_portfolio(filename):
    with open(filename) as f:
        headers = next(f)
        rows = csv.reader(f)
        for row in rows:
            try:
                holding = {'name' : row[0], 'shares' : int(row[1]), 'price' : float(row[2])}
                portfolio.append(holding)
            except:
                print("WARN: Cannot append row to portfolio list:", row)

    return portfolio

def read_prices(filename):
    with open(filename) as f:
        rows = csv.reader(f)

        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except:
                print("WARN: cannot set price of row reading", filename, ":", row)

    return prices

def calculate_profit() -> None:
    total = 0
    read_portfolio(sys.argv[1])
    read_prices(sys.argv[2])
    for holding in portfolio:
        try:
            holding_name = holding['name']
            # Calculate the difference of current price of holding from purchase price
            total += float((holding['shares']*prices[holding_name]) - (holding['shares']*holding['price']))
        except:
            print("WARN: Cannot calculate profit of holding:", holding)

    print("The total profit/loss is:", total)

if __name__ == '__main__':
    calculate_profit()
