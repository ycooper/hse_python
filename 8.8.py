import itertools
print(
    1,
    *itertools.accumulate(
        range(1, int(input()) + 1),
        lambda x, y: x * y
    )
)
