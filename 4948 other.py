memory=[1]*246913;memory[0]=memory[1]=0

for i in range(int(246912**(1/2))+1):
    if memory[i]:
        for p in range(i*2,246913,i):
            memory[p]=0
while True:
    n=int(input())
    if not n:break
    q=0
    for i in range(n+1,2*n+1):
        if memory[i] : q+=1
    print(q)