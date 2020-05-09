s = str(input())
pos = -1
pos2 = -1

pos = s.find("f")
n = pos

while n != -1:
    if n != pos:
        pos2 = n
    n = s.find("f", n + 1)

if pos != -1:
    if pos2 != -1:
        print("{} {}".format(pos, pos2))
    else:
        print(pos)
