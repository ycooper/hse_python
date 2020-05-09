a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

det = a * d - b * c
det1 = e * d - b * f
det2 = a * f - e * c

print("{} {}".format(det1 / det, det2 / det))
