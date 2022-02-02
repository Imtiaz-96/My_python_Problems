n=int(input())
l=list(map(int,input().split()))
a=[0,0,0]
b=["chest","biceps","back"]
for i in range(n):
    a[i%3]+=l[i]
print(b[a.index(max(a))])