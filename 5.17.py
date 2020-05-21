num_list = list(map(int, input().split()))
prev = num_list[0]
for i in num_list:
    if i > prev:
        print(i, end=" ")
    prev = i
