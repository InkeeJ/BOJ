from sys import stdin
raw_data=stdin.readlines()
rows=[list(map(int,_.split())) for _ in raw_data]
blank=[]
for i in range(9):
    for j in range(9):
        if rows[i][j]==0:blank.append((i,j))

n=len(blank)
def check(n,row,col):
    for x in range(9):
        if rows[row][x]==n:
            return True
        if rows[x][col]==n:
            return True
    i=row//3;j=col//3
    for x in range(3):
        for y in range(3):
            if rows[3*i+x][3*j+y]==n:
                return True

        
def sdoku(correct):
    if correct == n:
        for i in range(9):
            print(*rows[i])
        exit(0)
    else:
        i,j=blank[correct]
        for k in range(1,10):
            if check(k,i,j):
                continue
            else:
                rows[i][j]=k
                sdoku(correct+1)
                rows[i][j]=0
                        
sdoku(0)