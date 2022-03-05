from itertools import combinations
from math import comb


N = int(input())
board = []

for _ in range(N):
    board.append([int(x) for x in input().split()])


def get_team_power(players):
    """
    팀 선수들의 번호가 주어질 때, 팀의 능력치를 구한다.
    """
    global N, board

    total_power = 0

    for i in range(N // 2 - 1):
        for j in range(i + 1, N // 2):
            a, b = players[i], players[j]
            total_power += board[a][b]

    return total_power


for i in range(N - 1):
    for j in range(i + 1, N):
        board[i][j] += board[j][i]
        board[j][i] = 0

players_set = list(combinations(range(N), N // 2))
S_LEN = len(players_set)
min_diff = 123456789

for i in range(S_LEN // 2):
    team_a = players_set[i]
    team_b = players_set[S_LEN - 1 - i]

    diff = abs(get_team_power(team_a) - get_team_power(team_b))
    min_diff = min(min_diff, diff)

print(min_diff)
