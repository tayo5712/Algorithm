n, start = map(int, input().split())
dist = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


def dfs(st, t, num):
    global answer
    if t >= answer:
        return
    if num == n:
        answer = t
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                dfs(i, t + dist[st][i], num + 1)
                visited[i] = 0

answer = int(1e9)
visited = [0] * n
visited[start] = 1
dfs(start, 0, 1)
print(answer)
