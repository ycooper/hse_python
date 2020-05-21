def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(a * a, n / 2)
    else:
        return a * power(a, n - 1)


a = float(input())
n = int(input())
if n < 0:
    print(1 / power(a, -n))
else:
    print(power(a, n))
