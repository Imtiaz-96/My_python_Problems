n = int(input())
a = b = 1
while n > 0:
    b += 1
    a += b
    n -= a
print(b - 1)
