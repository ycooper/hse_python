def merge(a, b):
    a_len = len(a)
    b_len = len(b)
    a_counter = 0
    b_counter = 0
    result = []
    while a_counter < a_len and b_counter < b_len:
        if a[a_counter] < b[b_counter]:
            a_counter += 1
        elif a[a_counter] > b[b_counter]:
            b_counter += 1
        else:
            result.append(a[a_counter])
            a_counter += 1
            b_counter += 1
    return result

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
for i in merge(list_a, list_b):
    print(i, end=" ")
