a=input()
s='qwertyuiopasdfghjkl;zxcvbnm,./'
x=""
for i in input():
    if a=='R':
        x+=s[s.index(i)-1]
    else:  x+=s[s.index(i)+1]
print(x)
#The first output is so true <3