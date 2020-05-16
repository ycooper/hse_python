def sum(n):
    n = int(input())
    if n == 0:
        return n
    else:
        return n + sum(n)

n = 0
print(sum(n))
