num_list = list(map(int, input().split()))
counter = 1
length = len(num_list)
while counter < length:
    if counter % 2 != 0:
        print(num_list[counter], end=" ")
        print(num_list[counter - 1], end=" ")
    counter += 1
if (len(num_list) + 1) % 2 == 0:
    print(num_list[-1])
