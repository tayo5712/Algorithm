def bfs(i, j):
    q = []
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    q.append((i, j))

    while q:
        i, j = q.pop(0)

        if i == n-1 and j == m-1:
            return print(visited[i][j])

        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and miro[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))

n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]
bfs(0, 0)
