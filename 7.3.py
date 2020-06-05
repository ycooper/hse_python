a_list = list(map(int, input().split()))
a_set = set(a_list)

b_list = list(map(int, input().split()))
b_set = set(b_list)

print(*sorted(a_set & b_set))
