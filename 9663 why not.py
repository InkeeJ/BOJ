#https://www.acmicpc.net/source/37836327 참고하였음.
from sys import stdin
n=int(stdin.readline())
col = [True]*n
diagonal_right=diagonal_left=[True]*(2*n)
def check(i,j):
    return col[j] and diagonal_left[i+j] and diagonal_right[i-j]
    # Is (i,j)-position available? --> True or False
count=[0]
def go(row):
    if row==n: 
        count[0] +=1
        return
    for j in range(n if row else n//2):
        if not check(row,j): continue
        else:
            col[j]=diagonal_left[row+j]=diagonal_right[row-j]=False
            row +=1
            go(row)
            row -=1
            col[j]=diagonal_left[row+j]=diagonal_right[row-j]=True
if not n%2 :
    go(0)
    print(2*count[0])
if n%2:
    k=n//2
    go(0)
    count[0]=2*count[0]
    col[k]=diagonal_left[k]=diagonal_right[-k]=False
    go(1)
    print(count[0])