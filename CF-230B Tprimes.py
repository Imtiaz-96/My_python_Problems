n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(1,n+1):
    for j in range(a[i]):
        if a[j]%i==0:
            sum+=1
    if sum==3: print("YES")
    else: print("NO")