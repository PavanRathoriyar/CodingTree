n=int(input( ))
e=int(input())
p=[]
b=list()
print()
for i in range(n):
    p.append(int(input()))


for i in range(n):
    b.append(int(input()))
pb=dict(zip(p, b))
p.sort()
c=0
for i in range(n):
    if e>=p[i]:
        e+=pb[p[i]]
        c+=1
    else:
        return c
return c


