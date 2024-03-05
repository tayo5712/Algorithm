n, m = map(int, input().split())
woods = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
answer = 0

def dfs(i, j, sumV):
    global answer
    if j == m:
        i += 1
        j = 0
    if i == n:
        answer = max(answer, sumV)
        return
    if not visited[i][j]:
        visited[i][j] = 1
        for dr, dc in [[1, -1], [-1, -1], [-1, 1], [1, 1]]:
            nr, nc = i + dr, j + dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][j] and not visited[i][nc]:
                visited[nr][j] = 1
                visited[i][nc] = 1
                dfs(i, j + 1, sumV + woods[i][j] * 2 + woods[nr][j] + woods[i][nc])
                visited[nr][j] = 0
                visited[i][nc] = 0
        visited[i][j] = 0
    dfs(i, j + 1, sumV)
dfs(0, 0, 0)
print(answer)
