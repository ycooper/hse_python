def sum(a, b):
    if a == 0:
        print(b)
    elif b == 0:
        print(a)
    else:
        if a >= b:
            sum(a + 1, b - 1)
        else:
            sum(a - 1, b + 1)


a = int(input())
b = int(input())
sum(a, b)
