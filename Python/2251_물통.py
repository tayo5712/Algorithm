from collections import deque

A, B, C = map(int, input().split())


def bfs():
    answer = []
    visited = [[0] * (B + 1) for _ in range(A + 1)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1

    def pour(a, b):
        if not visited[a][b]:
            visited[a][b] = 1
            q.append((a, b))

    while q:
        a, b = q.popleft()
        c = C - (a + b)
        if a == 0:
            answer.append(c)
        water = min(a, B - b)
        pour(a - water, b + water)

        water = min(a, C - c)
        pour(a - water, b)

        water = min(b, A - a)
        pour(a + water, b - water)

        water = min(b, C - c)
        pour(a, b - water)

        water = min(c, A - a)
        pour(a + water, b)

        water = min(c, B - b)
        pour(a, b + water)

    return sorted(answer)

print(*bfs())
