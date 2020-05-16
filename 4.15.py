def gcd(a, b):
    if b == 0:
        return a
    else:
        if a < b:
            (a, b) = (b, a)
        return gcd(b, a % b)


a = int(input())
b = int(input())
print(gcd(a, b))
