new = 1
count = 0
s = 0

while new != 0:
    new = int(input())
    if new == 0:
        break
    s += new
    count += 1

print(s / count)
