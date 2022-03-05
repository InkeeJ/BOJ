import sys
n,m = tuple(map(int,input().split()))
#n : number of rows, m : number of columns
#WLOG, first index refers the order of row and second index so does to the order of column.
given_pattern = {}
for first_index in range(n):
    second_index=0
    for j in sys.stdin.readline().rstrip():
        given_pattern[(first_index,second_index)]=j
        second_index+=1
def data(starting_point:tuple):
    memory=[0]*64
    (i,j)=starting_point
    for first_index in range(8):
        for second_index in range(8):
            if first_index==0:
                if second_index==0: continue
                else:
                    if (given_pattern[(first_index+i,second_index+j)]==given_pattern[(first_index+i,second_index+j-1)] and memory[8*first_index+second_index-1]==0) or (given_pattern[(first_index+i,second_index+j)]!=given_pattern[(first_index+i,second_index+j-1)] and memory[8*first_index+second_index-1]==1): memory[8*first_index+second_index]=1
                    else:continue
            else:
                if second_index==0:
                    if (given_pattern[(first_index+i,second_index+j)]==given_pattern[(first_index+i-1,second_index+j)] and memory[8*(first_index-1)+second_index]==0) or (given_pattern[(first_index+i,second_index+j)]!=given_pattern[(first_index+i-1,second_index+j)] and memory[8*(first_index-1)+second_index]==1):memory[8*first_index+second_index]=1
                    else:continue
                else:
                    if (given_pattern[(first_index+i,second_index+j)]==given_pattern[(first_index+i,second_index+j-1)] and memory[8*first_index+second_index-1]==0) or (given_pattern[(first_index+i,second_index+j)]!=given_pattern[(first_index+i,second_index+j-1)] and memory[8*first_index+second_index-1]==1): memory[8*first_index+second_index]=1
                    else:continue
    data_0 = sum(memory)
    return min(data_0,64-data_0) 
datas=[0]*(n-7)*(m-7)
for i in range(n-7):
    for j in range(m-7):
        datas[i*(m-7)+j]=data((i,j))
print(min(datas))