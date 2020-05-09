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
elif (det == 0 and (det1 != 0 or det2 != 0)) or \
        (det != 0 and (det1 == 0 or det2 == 0)) or \
        (a == b == c == d == 0):
    print(0)
elif det1 != 0 or det2 != 0:
    print("2 {} {}".format(det1 / det, det2 / det))
else:
    if c == d == f == 0:
        if b != 0:
            if a != 0:
                print("1 {} {}".format(-a / b, e / b))
            else:
                print("4 {}".format(e / b))
        else:
            print("3 {}".format(e / a))
    elif a == b == e == 0:
        if d != 0:
            if c != 0:
                print("1 {} {}".format(-c / d, f / d))
            else:
                print("4 {}".format(f / d))
        else:
            print("3 {}".format(f / c))
    elif c == a == 0:
        if e == f == 0 and b % d == 0:
            if b != 0:
                if a != 0:
                    print("1 {} {}".format(-a / b, e / b))
                else:
                    print("4 {}".format(e / b))
            else:
                print("3 {}".format(e / a))
        elif e / f == b / d:
            if b != 0:
                if a != 0:
                    print("1 {} {}".format(-a / b, e / b))
                else:
                    print("4 {}".format(e / b))
            else:
                print("3 {}".format(e / a))
    elif b == d == 0:
        if e == f == 0 and a % c == 0:
            if b != 0:
                if a != 0:
                    print("1 {} {}".format(-a / b, e / b))
                else:
                    print("4 {}".format(e / b))
            else:
                print("3 {}".format(e / a))
        elif e / f == a / c:
            if b != 0:
                if a != 0:
                    print("1 {} {}".format(-a / b, e / b))
                else:
                    print("4 {}".format(e / b))
            else:
                print("3 {}".format(e / a))
    elif e == f == 0 and a / c == b / d:
        if b != 0:
            if a != 0:
                print("1 {} {}".format(-a / b, e / b))
            else:
                print("4 {}".format(e / b))
        else:
            print("3 {}".format(e / a))
    elif a / c == b / d == e / f:
        if b != 0:
            if a != 0:
                print("1 {} {}".format(-a / b, e / b))
            else:
                print("4 {}".format(e / b))
        else:
            print("3 {}".format(e / a))
