from collections import deque
INF = int(1e9)
tc = 1
while True:
    n = int(input())
    if n == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(n)]
    rupee = [[INF for _ in range(n)] for _ in range(n)]

    def bfs(str, stc):
        q = deque([(str, stc)])
        rupee[str][stc] = cave[str][stc]

        while q:
            r, c = q.popleft()
            for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < n and rupee[r][c] + cave[nr][nc] < rupee[nr][nc]:
                    q.append((nr, nc))
                    rupee[nr][nc] = rupee[r][c] + cave[nr][nc]
    bfs(0, 0)
    print(f'Problem {tc}: {rupee[n-1][n-1]}')
    tc += 1

