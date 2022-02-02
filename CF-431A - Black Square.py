a=list(map(int,input().split()))
s=list(map(int,input()))
sum=0
for i in s:
    sum+=a[(i)-1]
print(sum)