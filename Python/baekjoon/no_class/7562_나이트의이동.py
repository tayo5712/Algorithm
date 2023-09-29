from collections import deque

def bfs(now_r, now_c, goal_r, goal_c):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[now_r][now_c] = 1
    q = deque()
    q.append((now_r, now_c))
    while q:
        qr, qc = q.popleft()
        for dr, dc in [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]:
            nr, nc = qr + dr, qc + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = visited[qr][qc] + 1
                if nr == goal_r and nc == goal_c:
                    return visited[nr][nc] - 1
                q.append((nr, nc))

t = int(input())
for _ in range(t):
    n = int(input())
    now_r, now_c = map(int, input().split())
    goal_r, goal_c = map(int, input().split())
    if now_r == goal_r and now_c == goal_c:
        print(0)
    else:
        print(bfs(now_r, now_c, goal_r, goal_c))
