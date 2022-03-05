from sys import stdin
from math import floor
n=int(stdin.readline())
row = [True]*n
col = [True]*n
diagonal_right=[True]*(2*n-1)
diagonal_left=[True]*(2*n-1)

def check(i,j):
    return row[i] and col[j] and diagonal_left[i+j] and diagonal_right[i-j+n-1]
    #Is (i,j)-position available? --> True or False
s=[0] #the number of Q
row[0]=False
count=[0]
def go():
    # print('go')
    if s[0]==n-1: 
        count[0] +=1
        # print('really counted')
        return
    for i in range(1,n):
        if i>s[0]+1 : 
            # print('%dth row searched. There is no more possible outcomes #1' %(i-1))
            break
        if i <= row_memory[-1]: 
            # print('this is %ith row,'%i,'which is already determined')
            continue

        for j in range(n):
            if not check(i,j):
                # print(i,j, 'occupied')
                if j==n-1 and i>s[0]: 
                    # print('%dth row searched. There is no more possible outcomes #2' %i)
                    return
                else:continue
            else:
                s[0]+=1
                row_memory.append(i)
                # column_memory.append(j)
                row[i]=False
                col[j]=False
                diagonal_left[i+j]=False
                diagonal_right[i-j+n-1]=False
                # print(i,j, 'counted')
                # print('row memory :', row_memory)
                # print('# of Q : ', s[0])
                go()
                # print('out of 1 go')
                row_memory.pop()
                s[0]-=1
                # print('row memory :', row_memory)
                # print('# of Q : ', s[0])
                row[i]=True
                col[j]=True
                diagonal_left[i+j]=True
                diagonal_right[i-j+n-1]=True

if n%2 ==0 :
    for j in range(n//2):
        # print('execute investigating with %dth column'%j)
        row_memory=[0]
        col[j]=False
        diagonal_left[j]=False
        diagonal_right[-j+n-1]=False
        go()
        col[j]=True
        diagonal_left[j]=True
        diagonal_right[-j+n-1]=True
    print(2*count[0])
if n%2==1:
    k=floor(n/2)
    for j in range(k):
        # print('execute investigating with %dth column'%j)
        col[j]=False
        diagonal_left[j]=False
        diagonal_right[-j+n-1]=False
        row_memory=[0]
        go()
        col[j]=True
        diagonal_left[j]=True
        diagonal_right[-j+n-1]=True

    # print('symmetry part done')
    count[0]=2*count[0]
    # print('cetre part start')
    col[k]=False
    diagonal_left[k]=False
    diagonal_right[-k+n-1]=False
    row_memory=[0]
    go()
    print(count[0])