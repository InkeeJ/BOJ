a = int(input())
b = int(input())
m=b
memory=[0]*(m+1)
if a == b ==1:
    print(-1)    
else:        
    memory[2]=1
    for i in range(2,m+1):
        j=2
        while i%j!=0 and j<i:
            j+=1
            if j == i : memory[j]=1
    x=[]
    for i in range(a,b+1):
        if memory[i]==1:x.append(i)
    if x:
        print(sum(x))
        print(x[0])
    else:
        print(-1)