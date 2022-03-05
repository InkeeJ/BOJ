dict={}

import sys

def w(x:tuple):
    a,b,c=x
    if a<=0 or b<= 0 or c<= 0 : return 1
    elif a>20 or b>20 or c>20 : return 1048576
    elif x in dict:
        return dict[x]
    else:
        if a<b<c: 
            dict[(a,b,c)]= w((a,b,c-1))+w((a,b-1,c-1))-w((a,b-1,c))
            return dict[(a,b,c)]
        else: 
            dict[((a,b,c))]= w((a-1,b,c))+w((a-1,b-1,c))+w((a-1,b,c-1))-w((a-1,b-1,c-1))
            return dict[(a,b,c)]

while True:
    (a,b,c)=tuple(map(int,sys.stdin.readline().split()))
    if a == -1 and b == -1 and c == -1: break
    else: print('w(%s, %s, %s) =' %(a,b,c), w((a,b,c)))