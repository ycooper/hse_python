f = open('input.txt', 'r', encoding='utf8')
lines = f.readlines()
f.close()
lines1 = []
k = int(lines.pop(0)[:-1])
n = int(len(lines))
for l in lines:
    l = l[:-1]
    items = l.split(' ')
    items1 = (int(items[-1]), int(items[-2]), int(items[-3]))
    if items1[0] >= 40 and items1[1] >= 40 and items1[2] >= 40:
        lines1.append(items1[0] + items1[1] + items1[2])
lines1.sort()

if len(lines1) <= k:
    result = 0
elif k == 0 or len(lines1) == 0:
    result = 1
else:
    ans = [0] * 301
    for i in lines1:
        ans[i] += 1
    k1 = k
    index = 1
    for i in reversed(range(301)):
        if k1 - ans[i] >= 0:
            if ans[i] > 0:
                k1 -= ans[i]
                index = i
        else:
            break
    result = index

f = open('output.txt', 'w', encoding='utf8')
print(result, file=f)
f.close()
