import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
x=sorted(list((map(int,sys.stdin.readline().rstrip().split()))))

conditioned_number=0
outdoor=True
for i in range(n-2):
    if not outdoor: break
    for j in range(i+1,n-1):
        if not outdoor: break
        for k in range(j+1,n):
            (a,b,c)=(i,j,k)
            if x[a]+x[b]+x[c]==m : conditioned_number=m; outdoor=False;break
            elif conditioned_number<x[a]+x[b]+x[c]<m : conditioned_number=x[a]+x[b]+x[c]
print(conditioned_number)
