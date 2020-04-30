a = int(input())
b = int(input())
c = int(input())
if (a + b) % 2 == (a + c) % 2 == (b + c) % 2:
    print("NO")
else:
    print("YES")
