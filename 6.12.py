n = int(input())
l = []
for i in range(n):
    val = input().split()
    l.append((int(val[1]), str(val[0])))
l.sort(reverse=True)
for i in l:
    print(i[1])
