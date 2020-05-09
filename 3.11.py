a = float(input())
b = float(input())
c = float(input())
x1 = 0.0
x2 = 0.0
d = 0.0

d = b * b - 4 * a * c
if a == b == c == 0:
    print(3)
elif a == 0 and b != 0:
    x1 = -c / b
    print("1 {}".format(x1))
elif d >= 0 and a != 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)

    if x2 < x1:
        (x1, x2) = (x2, x1)
    if x1 != x2:
        print("2 {} {}".format(x1, x2))
    else:
        print("1 {}".format(x1))
else:
    print(0)
