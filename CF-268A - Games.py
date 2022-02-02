s,a=0,[input(). split() for _ in range(int(input()))]
for i in a:
	for j in a:
		if i[0]==j[1]: s+=1
print(s)