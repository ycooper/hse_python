num_list = list(map(int, input().split()))
min_positive = 1000
for i in num_list:
    if min_positive > i > 0:
        min_positive = i
print(min_positive)
