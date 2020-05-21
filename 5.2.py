a = int(input())
b = int(input())
order = 0
if b > a:
    order = 1
else:
    order = -1

for i in range(a, b + order, order):
    print(i, end=" ")
