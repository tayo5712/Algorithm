from collections import deque

F, S, G, U, D = map(int, input().split())

def bfs():
    q = deque()
    q.append((S, 0))
    visited = [0] * (F + 1)
    visited[S] = 1
    while q:
        now, cnt = q.popleft()
        if now == G:
            return cnt
        up = now + U
        down = now - D
        if up <= F and not visited[up]:
            q.append((up, cnt + 1))
            visited[up] = 1
        if down >= 1 and not visited[down]:
            q.append((down, cnt + 1))
            visited[down] = 1
    return "use the stairs"

print(bfs())

