for i in range(int(input())):
    (a,b)=tuple(map(int,input().split()))
    m=b-a
    k=m
    n=0
    while True:
        if n**2<m<(n+1)**2 : break
        if m == (n+1)**2 : step = 2*n+1;break 
        n=n+1
    m=m-n**2
    if k==(n+1)**2: print(step)
    elif (m-1)//n == 0 : print(2*n)
    elif (m-1)//n == 1 : print(2*n+1)