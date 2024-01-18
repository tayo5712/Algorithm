from collections import deque

def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0])
    q = deque()
    dist = [[int(1e9) for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                q.append((i, j, 0))
                dist[i][j] = 0
        if q:
            break

    while q:
        r, c, cnt = q.popleft()
        if board[r][c] == 'G':
            return cnt

        for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nr = r
            nc = c
            while 0 <= nr + dr < N and 0 <= nc + dc < M and board[nr + dr][nc + dc] != 'D':
                nr += dr
                nc += dc


            if dist[nr][nc] > cnt + 1:
                dist[nr][nc] = cnt + 1
                q.append((nr, nc, cnt + 1))

    return -1
