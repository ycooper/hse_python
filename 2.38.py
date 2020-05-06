m, c = 0, 0
new = int(input())

while new != 0:
    if new > m:
        m = new
        c = 1
    elif new == m:
        c += 1
    new = int(input())
print(c)
