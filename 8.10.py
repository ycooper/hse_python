import sys
import functools

print(
    *functools.reduce(
        lambda x, y: map(
            lambda a, b: a ^ b, x, y
        ),
        map(
            lambda line: map(
                int,
                line.split()
            ),
            sys.stdin.read().splitlines()[1:]
        )
    )
)
