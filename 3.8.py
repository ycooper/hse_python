n = int(input())
x = float(input())

value = 0
while n > 0:
    a = float(input())
    value = (value + a) * x
    n -= 1
a = float(input())
value = value + a
print(value)
