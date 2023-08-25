# https://level.goorm.io/exam/195692/gamejam/quiz/1
# 구름 챌린지 10일차

direction = {"U": 0, "D": 1, "L": 2, "R": 3}
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def play(n, r, c):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[r][c] = 1
    score = 1
    while True:
        dist = int(board[r][c][:-1])
        dir = board[r][c][-1]
        for _ in range(dist):
            r = (r + dr[direction[dir]]) % n
            c = (c + dc[direction[dir]]) % n
            if visited[r][c]:
                return score
            else:
                score += 1
                visited[r][c] = 1
        if score >= n * n:
            return score

N = int(input())
gr, gc = map(int, input().split())
pr, pc = map(int, input().split())
board = [list(input().split()) for _ in range(N)]

goorm_score = play(N, gr - 1, gc - 1)
player_score = play(N, pr - 1, pc - 1)

if goorm_score > player_score:
    print(f"goorm {goorm_score}")
else:
    print(f"player {player_score}")