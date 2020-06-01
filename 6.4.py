n = int(input())
l = sorted(list(map(int, input().split())))

result = 0
prev = 0
for i in l:
    if prev == 0 and i >= n:
        prev = i
        result += 1
        continue
    elif i - prev >= 3 and prev != 0:
        result += 1
        prev = i

print(result)
