p = int(input())
x = int(input())
y = int(input())
k = int(input())

n = x * 100 + y

i = 0
while i < k:
    n = (n + n * p // 100)
    i += 1
print("{} {}".format(n // 100, n % 100))
