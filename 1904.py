
n=int(input())
memory=[0]*(47245)
memory[1]=1
memory[2]=2
def f(n):
    n=n%47244
    if memory[n]: return memory[n]
    else: 
        memory[n]=(f(n-1)+f(n-2))%15746
        return memory[n]

k=n//500
i=1
while i<k:
    f(500*i);f(500*i+1)
    i+=1


print(f(n))