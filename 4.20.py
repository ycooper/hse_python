def reverse():
    n = int(input())
    if n == 0:
        print(0)
        return n
    else:
        reverse()
    print(n)


reverse()
