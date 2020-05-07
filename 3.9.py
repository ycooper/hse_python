new = 0.0
xsum = 0.0
x2sum = 0.0
s = 0.0
n = 0

new = float(input())
while new != 0:
    xsum += new
    x2sum += new * new
    n += 1
    new = float(input())

s = xsum / n
print(((x2sum - 2 * s * xsum + n * s * s) / (n - 1)) ** 0.5)
