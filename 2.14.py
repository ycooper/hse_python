a = int(input())
b = int(input())
c = int(input())
if c < a:
    (a, c) = (c, a)
if c < b:
    (b, c) = (c, b)
if b < a:
    (a, b) = (b, a)
print("{} {} {}".format(a, b, c))
