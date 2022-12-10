# 0 은 가로
# 1 은 세로
# 2 는 대각

def dfs(r, c, dir):
    global cnt
    if r == n-1 and c == n-1:
        cnt += 1
        return

    # 모든 방향에서 대각선 가능
    if 0 <= r + 1 < n and 0 <= c + 1 < n and board[r + 1][c + 1] != 1 and board[r][c + 1] != 1 and board[r + 1][c] != 1:
        dfs(r + 1, c + 1, 2)

    if dir == 0:    # 가로 방향일 때
        # 가로 -> 가로
        if 0 <= c+1 < n and board[r][c+1] != 1:
            dfs(r, c+1, 0)

    elif dir == 1:  # 세로 방향일 때
        # 세로 -> 세로
        if 0 <= r+1 < n and board[r+1][c] != 1:
            dfs(r+1, c, 1)

    elif dir == 2:  # 대각선 방향 일 때
        # 대각 -> 가로
        if 0 <= c+1 < n and board[r][c+1] != 1:
            dfs(r, c+1, 0)
        # 대각 -> 세로
        if 0 <= r+1 < n and board[r+1][c] != 1:
            dfs(r+1, c, 1)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
dfs(0, 1, 0)

print(cnt)