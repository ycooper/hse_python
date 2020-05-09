s = str(input())
l = len(s)
n = 0
while n < (l - 1):
    print(s[n], end="")
    print("*", end="")
    n += 1
print(s[l - 1])
