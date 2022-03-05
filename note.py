T=int(input())
memory=[0]*101
memory[0]=0
memory[1]=memory[2]=memory[3]=1
memory[4]=2
def p(n):
    if 0<=n<=4 : return memory[n]
    if not memory[n] : memory[n]=p(n-1)+p(n-5)
    return memory[n]

for i in range(T):
    n=int(input())
    print(p(n))
