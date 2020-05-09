s = str(input())
pos = s.find(" ")
print("{} {}".format(s[pos + 1:], s[:pos + 1]))
