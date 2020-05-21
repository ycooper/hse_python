num_list = list(map(int, input().split()))
current_max = num_list[0]
index = 0
max_index = 0
for i in num_list:
    if i >= current_max:
        current_max = i
        max_index = index
    index += 1
print("{} {}".format(current_max, max_index))
