n = int(input())
i = 1
s = 0.0

while i <= n:
    s += 1 / (i * i)
    i += 1
print("{0:6f}".format(s))
