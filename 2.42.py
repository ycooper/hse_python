count = 1
countmax = 0
new = int(input())
prev = 0

while new != 0:
    prev = new
    new = int(input())
    if new == prev:
        count += 1
    else:
        if count > countmax:
            countmax = count
        count = 1

if countmax == 0:
    countmax = count

print(countmax)
