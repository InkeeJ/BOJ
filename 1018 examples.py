from random import randint

H = randint(8,8)
W = randint(9,30)
RowList = []

for y in range(H):
    Temp = ''
    for x in range(W):
        random = randint(0,1)
        if random == 0:
            Temp += 'W'
        else:
            Temp += 'B'
    RowList.append(Temp)

print(H, W)
for i in RowList:
    print(i)