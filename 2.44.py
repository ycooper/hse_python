prev1 = 0
prev2 = 0
i = 0
i_prev_max = 0
distance = 0
distance_prev = 0

new = int(input())
while new != 0:
    if bool(prev1) and bool(prev2):
        if prev1 > new and prev1 > prev2:
            if i_prev_max != 0:
                if (i - i_prev_max < distance) or distance == 0:
                    distance = i - i_prev_max
            i_prev_max = i
    i += 1
    prev2 = prev1
    prev1 = new
    new = int(input())
print(distance)
