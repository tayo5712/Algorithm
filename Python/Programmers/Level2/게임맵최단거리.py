from collections import deque

def bfs(maps):
    q = deque([(0, 0)])
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _  in range(n)]
    visited[0][0] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                if nr == n - 1 and nc == m - 1:
                    return visited[nr][nc]
                q.append((nr, nc))
            
    return -1

def solution(maps):
    answer = bfs(maps)
    return answer
