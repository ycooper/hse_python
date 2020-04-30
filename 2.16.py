a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if c < a:
    (a, c) = (c, a)
if c < b:
    (b, c) = (c, b)
if b < a:
    (a, b) = (b, a)

if d > e:
    t = d
    d = e
    e = t

if a <= d and b <= e:
    print("YES")
else:
    print("NO")
