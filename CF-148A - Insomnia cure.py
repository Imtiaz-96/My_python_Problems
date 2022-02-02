k,l,m,n,d=[int(input())for i in range(5)]
x=0
for j in range(1,d+1):
    if (j%k==0) or (j%l==0) or (j%m==0) or (j%n==0):
        x+=1
print(x)
