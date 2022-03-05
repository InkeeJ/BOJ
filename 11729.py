n=int(input())
memory_1_3={1:[[0,2]], 2:[[0,1],[0,2],[1,2]]}
def sigma(x:tuple, y:list) -> list: 
    dict={}
    for i in range(len(x)):
        dict[i]=x[i]
    y_permuted=[]
    for i in range(len(y)):
        temp=[]
        for j in range(len(y[i])):
            temp.append(dict[y[i][j]])
        y_permuted.append(temp)
    return y_permuted
for i in range(3,n+1):
    memory_1_3[i]=memory_1_3[i-2]+[[0,1]]+sigma((2,0,1),memory_1_3[i-2])+[[0,2]]+sigma((1,0,2),memory_1_3[i-1])


print(len(memory_1_3[n]))
for i in memory_1_3[n]:
    (a,b)=i
    print(a+1,b+1)