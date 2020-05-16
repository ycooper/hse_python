def IsPrime(n):
    i = 2
    r = n ** (1 / 2)
    while i <= r:
        if n % i == 0:
            break
        i += 1
    if i > r:
        return "YES"
    return "NO"


n = int(input())
print(IsPrime(n))
