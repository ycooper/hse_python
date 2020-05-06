m, m2 = 0, 0
new = int(input())

while new != 0:
    if new > m:
        m2 = m
        m = new
    elif (m2 < new < m) or (new == m and m2 < new):
        m2 = new
    new = int(input())
print(m2)
