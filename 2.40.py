n1, n2 = 1, 0
a = int(input())
i = 2
c = 0

if a == 0:
    print(0)
elif a == 1:
    print(1)
else:
    while c < a:
        c = n1 + n2
        n2 = n1
        n1 = c
        i += 1
    if c == a:
        print(i - 1)
    else:
        print(-1)
