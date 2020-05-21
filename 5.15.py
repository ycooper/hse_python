count = 0
num_list = list(map(int, input().split()))
for i in num_list:
    if i > 0:
        count += 1
print(count)
