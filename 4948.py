while True:
    a=int(input())
    if not a: break
    b=2*a
    memory=[1]*(b+1)
    memory[0]=0 ; memory[1]=0
    for m in range(1,int(b**(1/2))+1):
        if memory[m]:
            for i in range(2*m,b+1,m):
                memory[i]=0
    p=0
    for i in range(a+1,b+1):
        if memory[i]: p+=1
    print(p)
