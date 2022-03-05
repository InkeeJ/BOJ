n=int(input())
a=list(map(int,input().split()))
m=max(a)

memory=[0]*(m+1)
memory[2]=1
for i in range(2,m+1):
    j=2
    while i%j!=0 and j<i:
        j+=1
        if j == i : memory[j]=1
result =0
for i in a:
    if memory[i]==1:result+=1
print(result)
