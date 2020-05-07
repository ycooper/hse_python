a = float(input())
b = float(input())
c = float(input())
x1 = 0.0
x2 = 0.0
d = 0.0

d = b * b - 4 * a * c
if d >= 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)

    if x2 < x1:
        (x1, x2) = (x2, x1)
    if x1 != x2:
        print("{} {}".format(x1, x2))
    else:
        print(x1)
