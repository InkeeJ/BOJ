N, M = map(int, input().split())
chess = []
for _ in range(N):
    chess.append(list(input()))

for i in range(N):
    for j in range(M):
        if chess[i][j] == 'W':
            chess[i][j] = 0
        else:
            chess[i][j] = 1

min_paint = 64

for i in range(N - 7):
    for j in range(M - 7):
        paint = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                paint += ((x - i) + (y - j) - chess[x][y]) % 2
        if paint > 32:
            paint = 64 - paint
        min_paint = min(min_paint, paint)

print(min_paint)