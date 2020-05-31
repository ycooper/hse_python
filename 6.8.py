f = open('input.txt', 'r', encoding='utf8')
lines = f.readlines()
f.close()
lines1 = []
for l in lines:
    l = l[:-1]
    items = l.split(' ')
    items1 = (items[0], items[1], items[3])
    items2 = ' '.join(items1)
    lines1.append(items2)
lines1.sort()
f = open('output.txt', 'w', encoding='utf8')
for l in lines1:
    print(l, file=f)
f.close()
