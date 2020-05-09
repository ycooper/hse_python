s = str(input())
l = len(s)
n = 0
while n < l:
    if n % 3 == 0:
        n += 1
        continue
    else:
        print(s[n], end="")
    n += 1
