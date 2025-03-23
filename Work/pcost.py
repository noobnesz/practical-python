# pcost.py
#
# Exercise 1.27
import csv
import sys



def portfolio_cost(filename):
    """
    Calculates portfolio cost.
    """
    total = 0

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            try:
                print("INFO: Parsing line:", row)
                price = (float(row[2]))*(int(row[1]))
                total += price
            except ValueError:
                print("WARN: Cannot parse line:", row)

    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost', cost)