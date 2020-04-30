l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())

s1 = r1 - l1
s2 = r2 - l2
s3 = r3 - l3
d12, d13, d23 = 0, 0, 0

if r1 < l2:
    d12 = l2 - r1
elif r2 < l1:
    d12 = l1 - r2

if r1 < l3:
    d13 = l3 - r1
elif r3 < l1:
    d13 = l1 - r3

if r2 < l3:
    d23 = l3 - r2
elif r3 < l2:
    d23 = l2 - r3

if (d12 == d13 == 0) or (d12 == d23 == 0) or (d13 == d23 == 0):
    print(0)
elif s1 >= d23:
    print(1)
elif s2 >= d13:
    print(2)
elif s3 >= d12:
    print(3)
else:
    print(-1)
