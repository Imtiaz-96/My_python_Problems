num = int(input())
F = []
a, b = 0, 1
F.append(a)
for _ in range(num+1):
    F.append(b)
    a, b = b, a + b
print(sum(F[:num+1]))