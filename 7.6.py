import sys
myset = set()

for line in sys.stdin:
    for j in list(map(str, line.split())):
        myset.add(j)

print(len(myset))
