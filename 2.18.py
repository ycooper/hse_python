a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
n, nt = 0, 0

nt = (a1 // a2) * (b1 // b2) * (c1 // c2)
if nt > n:
    n = nt

nt = (a1 // b2) * (b1 // c2) * (c1 // a2)
if nt > n:
    n = nt

nt = (a1 // c2) * (b1 // a2) * (c1 // b2)
if nt > n:
    n = nt

nt = (a1 // a2) * (b1 // c2) * (c1 // b2)
if nt > n:
    n = nt

nt = (a1 // b2) * (b1 // a2) * (c1 // c2)
if nt > n:
    n = nt

nt = (a1 // c2) * (b1 // b2) * (c1 // a2)
if nt > n:
    n = nt

print(n)
