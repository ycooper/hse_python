a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == b == 0:
    print("INF")
elif a != 0:
    if c != 0:
        if -d / c != -b / a and -b / a % 1 == 0:
            print(-b // a)
        else:
            print("NO")
    elif -b / a % 1 == 0:
        print(-b // a)
    else:
        print("NO")
else:
    print("NO")
