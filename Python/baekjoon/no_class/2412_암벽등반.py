from collections import deque

def bfs():
    visited = set()
    q = deque([(0, 0, 0)])
    while q:
        x, y, cnt = q.popleft()
        if y == t:
            return cnt
        for i in range(-2, 3):
            for j in range(-2, 3):
                nx = x + i
                ny = y + j
                if (nx, ny) in pos and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny, cnt + 1))
    return -1

n, t = map(int, input().split())
pos = set(tuple(map(int, input().split())) for _ in range(n))

print(bfs())
