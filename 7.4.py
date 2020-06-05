a_list = list(map(int, input().split()))
a_set = set()

for i in a_list:
    if i in a_set:
        print("YES")
    else:
        print("NO")
        a_set.add(i)
