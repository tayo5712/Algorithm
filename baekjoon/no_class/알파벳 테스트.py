from collections import deque

def bfs(sti, stj):
    person = deque([(sti, stj, 1)])
    visited_p = [[0] * m for _ in range(n)]
    visited_p[sti][stj] = 1
    while person:
        pi, pj, pcnt = person.popleft()
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            npi = pi + di
            npj = pj + dj
            if npi < 0 or npi >= n or npj < 0 or npj >= m:
                return pcnt
            if building[npi][npj] == '.' and not visited_p[npi][npj]:
                visited_p[npi][npj] = 1
                person.append((npi, npj, pcnt+1))
        if fire:
            fi, fj = fire.popleft()
            for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nfi = fi + di
                nfj = fj + dj
                if nfi < 0 or nfi >= n or nfj < 0 or nfj >= m:
                    return 'IMPOSSIBLE'
                if building[nfi][nfj] == '.' and not visited_f[nfi][nfj]:
                    visited_f[nfi][nfj] = 1
                    fire.append((nfi, nfj))
    return 'IMPOSSIBLE'

for _ in range(int(input())):
    m, n = map(int, input().split())
    building = [list(input()) for _ in range(n)]
    fire = deque()
    visited_f = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if building[i][j] == '@':
                sti, stj = i, j
                building[sti][stj] = '.'

            if building[i][j] == '*':
                fire.append((i, j))
                visited_f[i][j] = 1

    print(bfs(sti, stj))