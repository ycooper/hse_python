l1 = int(input())
w1 = int(input())
h1 = int(input())
l2 = int(input())
w2 = int(input())
h2 = int(input())
lc = int(input())
wc = int(input())
hc = int(input())
possible = False

if ((l1 + l2 <= lc) and w1 <= wc and w2 <= wc) \
        or ((w1 + w2 <= wc) and l1 <= lc and l2 <= lc) or (h1 + h2 <= hc):
    possible = True

l2, w2 = w2, l2
if ((l1 + l2 <= lc) and w1 <= wc and w2 <= wc) \
        or ((w1 + w2 <= wc) and l1 <= lc and l2 <= lc) or (h1 + h2 <= hc):
    possible = True

l1, w1 = w1, l1
if ((l1 + l2 <= lc) and w1 <= wc and w2 <= wc) \
        or ((w1 + w2 <= wc) and l1 <= lc and l2 <= lc) or (h1 + h2 <= hc):
    possible = True

l2, w2 = w2, l2
if ((l1 + l2 <= lc) and w1 <= wc and w2 <= wc) \
        or ((w1 + w2 <= wc) and l1 <= lc and l2 <= lc) or (h1 + h2 <= hc):
    possible = True

if not (h1 <= hc and h2 <= hc) or (l1 > lc and l1 > wc) or \
        (l2 > lc and l2 > wc) or (w1 > lc and w1 > wc) or \
        (w2 > lc and w2 > wc):
    possible = False

if possible:
    print("YES")
else:
    print("NO")
