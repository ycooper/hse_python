a = int(input())
n = 1
k = 1
i = 1
s = ''
c = 0

while n <= a:
    s = ''
    i = 1
    k = 1
    while n // k > 0:
        s += str(n)[-i]
        k *= 10
        i += 1
    if str(n) == s:
        c += 1
    n += 1
print(c)
