k = int(input())
m = int(input())
n = int(input())

if n > k:
    print(m * ((n * 2) // k + int(bool((n * 2) % k))))
else:
    print(2 * m)
