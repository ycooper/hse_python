s = str(input())
pos = -1
pos2 = -1

pos = s.find("h")
n = pos

while n != -1:
    if n != pos:
        pos2 = n
    n = s.find("h", n + 1)

print("{}{}".format(s[0:pos], s[pos2 + 1:]))
