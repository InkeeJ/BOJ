memory = [0]*1415



def f(m,n):
    k=100*m+n
    if m ==0: memory[k] = n
    if memory[k] !=0 : return memory[k]
    else:
        y=0
        for i in range(1,n+1):
            y += f(m-1,i)
        memory[k]=y
        return memory[k]
        

for i in range(int(input())):
    m=int(input())
    n=int(input())
    print(f(m,n))