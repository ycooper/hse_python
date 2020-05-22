n = int(input())
num_list = list(map(int, input().split()))
x = int(input())
diff = abs(x - num_list[0])
value = num_list[0]
for i in num_list:
    cur_diff = abs(x - i)
    if cur_diff < diff:
        diff = cur_diff
        value = i
print(value)
