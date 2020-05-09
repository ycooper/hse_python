a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

det = a * d - b * c
det1 = e * d - b * f
det2 = a * f - e * c

if a == b == c == d == e == f == 0:
    print(5)
elif a == b == c == d == 0:
    print(0)
elif det != 0:
    print("2 {} {}".format(det1 / det, det2 / det))
elif a == b == 0:
    if e != 0:
        print(0)
    else:
        if c != 0 and d != 0:
            print("1 {} {}".format(-c / d, f / d))
        elif c != 0 and d == 0:
            print("3 {}".format(f / c))
        elif c == 0 and d != 0:
            print("4 {}".format(f / d))
elif c == d == 0:
    if f != 0:
        print(0)
    else:
        if a != 0 and b != 0:
            print("1 {} {}".format(-a / b, e / b))
        elif a != 0 and b == 0:
            print("3 {}".format(e / a))
        elif a == 0 and b != 0:
            print("4 {}".format(e / b))
elif a == c == 0:
    if b != 0 and e != 0 and d != 0 and f != 0:
        if e / f == b / d:
            print("4 {}".format(e / b))
        else:
            print(0)
    elif b != 0 and e != 0 and d == 0 and f == 0:
        print("4 {}".format(e / b))
    elif b != 0 and e == 0 and d != 0 and f == 0:
        print("4 {}".format(e / b))
    elif b == 0 and e == 0 and d != 0 and f != 0:
        print("4 {}".format(f / d))
    else:
        print(0)
elif b == d == 0:
    if a != 0 and e != 0 and c != 0 and f != 0:
        if e / f == a / c:
            print("3 {}".format(e / a))
        else:
            print(0)
    elif a != 0 and e != 0 and c == 0 and f == 0:
        print("3 {}".format(e / a))
    elif a != 0 and e == 0 and c != 0 and f == 0:
        print("3 {}".format(e / a))
    elif a == 0 and e == 0 and c != 0 and f != 0:
        print("3 {}".format(f / c))
    else:
        print(0)
elif e == f == 0:
    if a / c == b / d:
        print("1 {} {}".format(-a / b, e / b))
    else:
        print(0)
elif a / c == b / d == e / f:
    print("1 {} {}".format(-a / b, e / b))
elif det == 0:
    print(0)
