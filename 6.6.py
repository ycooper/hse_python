def dist(a, b):
    return abs(a - b)

n = int(input())
villages = list(map(int, input().split()))
vil = []
for i in range(len(villages)):
    vil.append((villages[i], i))
vil.sort()

m = int(input())
shelters = list(map(int, input().split()))
sh = []
for i in range(len(shelters)):
    sh.append((shelters[i], i))
sh.sort()

answer = [None] * n
index = 0
for i in vil:
    while index <= m - 2 and \
            dist(i[0], sh[index][0]) > dist(i[0], sh[index + 1][0]):
        index += 1
    answer[i[1]] = sh[index][1] + 1

print(*answer)
