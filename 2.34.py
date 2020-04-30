new = 1
count = 0
prev = 0

new = int(input())
while new != 0:
    prev = new
    new = int(input())
    if new == 0:
        break
    if new > prev:
        count += 1

print(count)
