def dfs(i, j, cnt):
    global maxV
    if cnt > maxV:
        maxV = cnt

    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ni = i + di
        nj = j + dj
        if 0 <= ni < n and 0 <= nj < m and not alpha[ord(board[ni][nj])-ord('A')]:
            alpha[ord(board[ni][nj])-ord('A')] = True
            dfs(ni, nj, cnt + 1)
            alpha[ord(board[ni][nj])-ord('A')] = False

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
maxV = 0
alpha = [False] * 26
alpha[ord(board[0][0])-ord('A')] = True
dfs(0, 0, 1)
print(maxV)