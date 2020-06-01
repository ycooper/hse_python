def countSort(a):
    ans = [0] * 101
    b = []
    for i in a:
        ans[i] += 1
    for val in range(len(ans)):
        for i in range(ans[val]):
            b.append(val)
    return b

l = list(map(int, input().split()))
print(*countSort(l))
