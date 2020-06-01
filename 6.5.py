s, n = list(map(int, input().split()))
l = []
for i in range(n):
    l.append(int(input()))
l.sort()

data = 0
count = 0
for i in l:
    if i + data < s:
        data += i
        count += 1
    else:
        break

print(count)
