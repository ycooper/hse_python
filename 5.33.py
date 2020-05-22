num_list = list(map(int, input().split()))
min_val = num_list[0]
min_index = 0
max_val = num_list[0]
max_index = 0
counter = 0

for i in num_list:
    if i < min_val:
        min_val = i
        min_index = counter
    elif i > max_val:
        max_val = i
        max_index = counter
    counter += 1

num_list.pop(min_index)
num_list.insert(min_index, max_val)
num_list.pop(max_index)
num_list.insert(max_index, min_val)
for i in num_list:
    print(i, end=" ")
