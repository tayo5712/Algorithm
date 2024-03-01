from collections import deque

def find_cheese():
    while air:
        r, c = air.popleft()
        for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n + 2 and 0 <= nc < m + 2 and not visited[nr][nc]:
                # 공기
                if board[nr][nc] == 0:
                    air.append((nr, nc))
                # 치즈
                else:
                    cheese.add((nr, nc))
                visited[nr][nc] = 1

n, m = map(int, input().split())
board = [[0] * (m + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (m + 2)]
visited = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
air = deque([(0, 0)])
before_cheese = 0
cheese = set()
visited[0][0] = 1
day = 0
while True:

    find_cheese()
    if len(cheese) == 0:
        print(day)
        print(before_cheese)
        break
    day += 1
    air = deque(cheese)
    before_cheese = len(cheese)
    cheese = set()
