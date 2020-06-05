input_line = ""
n = int(input())

positive_set = set(i for i in range(1, n + 1))
negative_set = set()

input_set = input()
while input_set != "HELP":
    input_line = str(input())
    if input_line == "YES":
        positive_set &= set(map(int, input_set.split()))
    elif input_line == "NO":
        negative_set |= set(map(int, input_set.split()))
    input_set = input()

print(*sorted(positive_set - negative_set))
