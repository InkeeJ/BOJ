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


memory=[0]*64
(i,j)=(0,0)
for first_index in range(8):
    for second_index in range(8):
        x_prev_vertical=8*(first_index-1)+second_index
        x=8*first_index+second_index ; x_prev_horizontal=x-1
        if first_index==0:
            if second_index==0: continue
            else:
                if (given_pattern[(first_index+i,second_index+j)]==given_pattern[(first_index+i,second_index+j-1)] and memory[x_prev_horizontal]==0) or (given_pattern[(first_index+i,second_index+j)]!=given_pattern[(first_index+i,second_index+j-1)] and memory[x_prev_horizontal]==1): memory[x]=1
                else:continue
        else:
            if second_index==0:
                if (given_pattern[(first_index+i,second_index+j)]==given_pattern[(first_index+i-1,second_index+j)] and memory[x_prev_vertical]==0) or (given_pattern[(first_index+i,second_index+j)]!=given_pattern[(first_index+i-1,second_index+j)] and memory[x_prev_vertical]==1):memory[x]=1
                else:continue
            else:
                if (given_pattern[(first_index+i,second_index+j)]==given_pattern[(first_index+i,second_index+j-1)] and memory[x_prev_horizontal]==0) or (given_pattern[(first_index+i,second_index+j)]!=given_pattern[(first_index+i,second_index+j-1)] and memory[x_prev_horizontal]==1): memory[x]=1
                else:continue
data_0 = sum(memory)
data=min(data_0,64-data_0)

datas=[0]*(n-7)*(m-7)
if n==8 and m==8: datas[0]=data
elif n==8 and m>8:
    i=0
    datas[0]=data
    temp_memory=memory
    for j in range(m-8):
        if temp_memory[1]==1:
            for first_index in range(8): #move horizontally by one step changing 1 to 0 and 0 to 1 of original information
                for second_index in range(1,8):
                    y=first_index*8+second_index
                    z=temp_memory[y]
                    if z==1:temp_memory[y-1]=0
                    else:temp_memory[y-1]=1
        else :
            for first_index in range(8): #move horizontally by one step invariantly
                for second_index in range(1,8):
                    y=first_index*8+second_index;temp_memory[y-1]=temp_memory[y]
        second_index=7
        for first_index in range(8): #add rightmost column information
            x=8*first_index+second_index ; x_prev_horizontal=x-1
            if (given_pattern[(first_index+i,second_index+j+1)]==given_pattern[(first_index+i,second_index+j)] and temp_memory[x_prev_horizontal]==0) or (given_pattern[(first_index+i,second_index+j+1)]!=given_pattern[(first_index+i,second_index+j)] and temp_memory[x_prev_horizontal]==1): temp_memory[x]=1
            else: temp_memory[x]=0
        data_0=sum(temp_memory)
        data=min(data_0,64-data_0)
        datas[j+1]=data
elif n>8 and m==8:
    for i in range(n-8):
        datas[i]=data
        if memory[8]==1: #changing 1 to 0 & 0 to 1
            for first_index in range(1,8):
                for second_index in range(8):
                    y=first_index*8+second_index
                    z=memory[y]
                    if z==1:memory[y-8]=0
                    else:memory[y-8]=1
            else : #invariantly
                for first_index in range(1,8):
                    for second_index in range(8):
                        y=first_index*8+second_index;memory[y-8]=memory[y]
            first_index=7 #set an updated memory for the next step
            for second_index in range(8):
                x_prev_vertical=8*(first_index-1)+second_index
                x=8*first_index+second_index
                if (given_pattern[(first_index+i+1,second_index+j)]==given_pattern[(first_index+i,second_index+j)] and memory[x_prev_vertical]==0) or (given_pattern[(first_index+i+1,second_index+j)]!=given_pattern[(first_index+i,second_index+j)] and memory[x_prev_vertical]==1):memory[x]=1
                else:memory[x]=0
            data_0=sum(memory)
            data=min(data_0,64-data_0)
    i=n-8 #Last row
    datas[i]=data
elif n>8 and m>8:
    for i in range(n-8):
        datas[i*(m-7)]=data
        temp_memory=memory
        for j in range(m-8):
            if temp_memory[1]==1:
                for first_index in range(8): #move horizontally by one step changing 1 to 0 and 0 to 1 of original information
                    for second_index in range(1,8):
                        y=first_index*8+second_index
                        z=temp_memory[y]
                        if z==1:temp_memory[y-1]=0
                        else:temp_memory[y-1]=1
            else :
                for first_index in range(8): #move horizontally by one step invariantly
                    for second_index in range(1,8):
                        y=first_index*8+second_index;temp_memory[y-1]=temp_memory[y]
            second_index=7
            for first_index in range(8): #add rightmost column information
                x=8*first_index+second_index ; x_prev_horizontal=x-1
                if (given_pattern[(first_index+i,second_index+j+1)]==given_pattern[(first_index+i,second_index+j)] and temp_memory[x_prev_horizontal]==0) or (given_pattern[(first_index+i,second_index+j+1)]!=given_pattern[(first_index+i,second_index+j)] and temp_memory[x_prev_horizontal]==1): temp_memory[x]=1
                else: temp_memory[x]=0
            data_0=sum(temp_memory)
            data=min(data_0,64-data_0)
            datas[i*(m-7)+j+1]=data
        #after investigating a row, move vertically down
        if memory[8]==1: #changing 1 to 0 & 0 to 1
            for first_index in range(1,8):
                for second_index in range(8):
                    y=first_index*8+second_index
                    z=memory[y]
                    if z==1:memory[y-8]=0
                    else:memory[y-8]=1
        else : #invariantly
            for first_index in range(1,8):
                for second_index in range(8):
                    y=first_index*8+second_index;memory[y-8]=memory[y]
        first_index=7 #set an updated memory for the next step
        for second_index in range(8):
            x_prev_vertical=8*(first_index-1)+second_index
            x=8*first_index+second_index
            if (given_pattern[(first_index+i+1,second_index+j)]==given_pattern[(first_index+i,second_index+j)] and memory[x_prev_vertical]==0) or (given_pattern[(first_index+i+1,second_index+j)]!=given_pattern[(first_index+i,second_index+j)] and memory[x_prev_vertical]==1):memory[x]=1
            else:memory[x]=0
        data_0=sum(memory)
        data=min(data_0,64-data_0)
    i=n-8 #Last row
    datas[i*(m-7)]=data
    temp_memory=memory
    for j in range(m-8):
        if temp_memory[1]==1:
            for first_index in range(8): #move horizontally by one step changing 1 to 0 and 0 to 1 of original information
                for second_index in range(1,8):
                    y=first_index*8+second_index
                    z=temp_memory[y]
                    if z==1:temp_memory[y-1]=0
                    else:temp_memory[y-1]=1
        else :
            for first_index in range(8): #move horizontally by one step invariantly
                for second_index in range(1,8):
                    y=first_index*8+second_index;temp_memory[y-1]=temp_memory[y]
        second_index=7
        for first_index in range(8): #add rightmost column information
            x=8*first_index+second_index ; x_prev_horizontal=x-1
            if (given_pattern[(first_index+i,second_index+j+1)]==given_pattern[(first_index+i,second_index+j)] and temp_memory[x_prev_horizontal]==0) or (given_pattern[(first_index+i,second_index+j+1)]!=given_pattern[(first_index+i,second_index+j)] and temp_memory[x_prev_horizontal]==1): temp_memory[x]=1
            else: temp_memory[x]=0
        data_0=sum(temp_memory)
        data=min(data_0,64-data_0)
        datas[i*(m-7)+j+1]=data


        
print(min(datas))