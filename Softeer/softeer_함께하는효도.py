from itertools import product
def check(routes):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    score = 0
    for route in routes:
        for nr, nc in route:
            if not visited[nr][nc]:
                visited[nr][nc] = 1
                score += arr[nr][nc]
            else:
                return 0
    return score
def dfs(path, r, c, routes):
    if len(path) == 4:
        routes.append(path[:])
        return
    else:
        for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in path:
                path.append((nr, nc))
                dfs(path, nr, nc, routes)
                path.pop()

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
friends_routes = []

for _ in range(k):
    r, c = map(int, input().split())
    routes = []
    dfs([(r - 1, c - 1)], r - 1, c - 1, routes)
    friends_routes.append(routes)

ans = 0
for routes in product(*friends_routes):
    ans = max(ans, check(routes))
print(ans)
