def sigma(x:tuple, y:list) -> list: #y is consisting of lists of length less than or equal to the length of the tuple x.
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


print(sigma((1,0,2),[[1,2],[0,1],[0,2]]))
