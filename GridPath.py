n=int(input())
a=[]
for i in range(n):
    a.append([int(j) for j in input().split()])
r=max(a[0])
t=r
a.pop(0)
for i in a:
    if max(i)>r:
        t+=max(i)
        r=max(i)
    else:
        break
print(t)
    
    
