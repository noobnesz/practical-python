# pcost.py
#
# Exercise 1.27
total = 0

with open('Data/portfolio.csv') as f:
    next(f)
    for line in f:
        row = line.split(',')
        price = (float(row[2].strip()))*(int(row[1]))
        total += price

print(f'Total cost {total}')