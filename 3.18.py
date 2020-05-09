s = str(input())
pos = -1
pos2 = -1

pos = s.find("f")
n = pos

while n != -1:
    if n != pos:
        pos2 = n
        break
    n = s.find("f", n + 1)

if pos2 != -1:
    print(pos2)
elif pos != -1:
    print(-1)
else:
    print(-2)
