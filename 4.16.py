def gcd(a, b):
    if b == 0:
        return a
    else:
        if a < b:
            (a, b) = (b, a)
        return gcd(b, a % b)


def ReduceFraction(n, m):
    d = gcd(n, m)
    if d == 1:
        return m, n
    else:
        return ReduceFraction(n // d, m // d)


m = int(input())
n = int(input())
print(*ReduceFraction(n, m))
