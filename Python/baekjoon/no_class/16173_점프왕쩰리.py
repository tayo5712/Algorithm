from collections import deque

def bfs():
    visited = [[0 for _ in range(n)] for _  in range(n)]
    visited[0][0] = 1
    q = deque([(0, 0)])

    while q:
        r, c = q.popleft()
        step = arr[r][c]
        if step == -1:
            return "HaruHaru"
        for dr, dc in [(1, 0), (0, 1)]:
            nr = r + dr * step
            nc = c + dc * step
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))
    return "Hing"

n = int(input())
arr = [list(map(int, input().split())) for _  in range(n)]
print(bfs())

