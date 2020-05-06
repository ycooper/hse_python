from math import ceil

n = float(input())

if n % 0.5 == 0:
    print(ceil(n))
else:
    print(round(n))
