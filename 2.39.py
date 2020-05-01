n1, n2 = 1, 0
n = int(input())
i = 2
c = 0

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    while i <= n:
        c = n1 + n2
        n2 = n1
        n1 = c
        i += 1
    print(c)
