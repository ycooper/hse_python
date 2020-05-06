count = 1
countmax = 0
new = int(input())
prev = 0
increasing = 0

while new != 0:
    prev = new
    new = int(input())
    if new == 0:
        break
    if new > prev and increasing >= 0:
        count += 1
        increasing = 1
    elif new < prev and increasing <= 0:
        count += 1
        increasing = -1
    elif new == prev:
        count = 1
        increasing = 0
    else:
        count = 2
        increasing *= -1
    if count > countmax:
        countmax = count

if countmax == 0:
    countmax = count

print(countmax)
