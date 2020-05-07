p = int(input())
x = int(input())
y = int(input())

n = x * 100 + y
n = (n + n * p // 100)
print("{} {}".format(n // 100, n % 100))
