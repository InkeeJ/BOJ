import math
for m in range(int(input())):
    (a,b)=tuple(map(int,input().split()))
    m=b-a
    d=math.sqrt(m)
    n=math.floor(d)
    m=round(d)
    if n == d: print(2*n-1)
    elif n == m: print(2*n)
    elif n < m : print(2*n+1)
