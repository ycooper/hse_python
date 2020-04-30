new = 1
count = 0

while new != 0:
    new = int(input())
    if new == 0:
        break
    if new % 2 == 0:
        count += 1

print(count)
