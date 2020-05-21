def flag(n):
    print("+___ " * n)
    for i in range(1, n + 1):
        print("|{} / ".format(i), end="")
    print()
    print("|__\ " * n)
    print("|    " * n)


n = int(input())
flag(n)
