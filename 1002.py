first_line = input()
output=[]
for i in range(int(first_line)):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1-x2)**2+(y1-y2)**2)
    R=max(r1, r2)
    r=min(r1, r2)
    if r == R and d == 0:
        result = -1
    elif d > (R+r)**2 or d < (R-r)**2:
        result = 0
    elif (R-r)**2 < d < (R+r)**2:
        result = 2
    elif d == (R-r)**2 or d == (R+r)**2 :
        result = 1
    output.append(result)
for i in range(int(first_line)):
    print(output[i])
    