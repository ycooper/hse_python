import itertools
print(
    "\n".join(
        map(
            lambda x: ''.join(map(str, x)),
            itertools.permutations(
                range(
                    1,
                    int(input()) + 1
                )
            )
        )
    )
)
