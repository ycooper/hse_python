def IsPointInArea(x, y):
    return (((x + 1) * (x + 1) + (y - 1) * (y - 1)) <= 4 and
            (y >= -x and y >= 2 * x + 2)) or \
           (not (((x + 1) * (x + 1) + (y - 1) * (y - 1)) < 4) and
            (y <= -x and y <= 2 * x + 2))


x = float(input())
y = float(input())
if IsPointInArea(x, y):
    print("YES")
else:
    print("NO")
