n,k = map(int, input().split())
for i in range(n):
    x = [0] * n
    x[i]=k
    print(*x)
