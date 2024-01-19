n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1 for _ in range(m)] for _ in range(n)]

def dfs(r, c):
    if r == n - 1 and c == m - 1:
        return 1
    if dp[r][c] == -1:
        dp[r][c] = 0
        for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] < arr[r][c]:
                dp[r][c] += dfs(nr, nc)
    return dp[r][c]

print(dfs(0, 0))
