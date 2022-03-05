n=int(input())
m=n//2
import sys
rows=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
total=sum([sum(x) for x in rows])
players={_ for _ in range(n)}
team=[]
def team_up(k,x : list):
    for i in range(1,n):
        if k==m:
            team.append(tuple(x))
            team.append(tuple(players-set(x)))
            return
        else:
            if i<=x[-1]: continue
            else:
                x.append(i)
                team_up(k+1, x)
                x.pop()


def stat(k,i,j,num):
    i=team[k][i]
    j=team[k][j]
    num=num+rows[i][j]+rows[j][i]
    return num





team_up(1, [0])
a=team[-1]
min=2000
k=0
outdoor = 0
while not outdoor==a:
    outdoor=team[k+1]
    num1=num2=0
    for i in range(m):
        for j in range(m):
            if j<=i : continue
            num1=stat(k,i,j,num1)
            num2=stat(k+1,i,j,num2)


    answer = abs(num1-num2)
    if min>answer:min=answer
    k +=2
print(min)
