"""n=int(input())
s1=list(map(int, input().split()))
s2=list(map(int, input().split()))
s3=list(map(int, input().split()))
print(sum(s1)-sum(s2))
print(sum(s2)-sum(s3))"""
n=int(input())
s1,s2,s3=[sum((map(int, input().split()))) for i in range(3)]
print(s1-s2)
print(s2-s3)
