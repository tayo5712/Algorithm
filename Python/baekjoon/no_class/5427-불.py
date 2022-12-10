from collections import deque

def bfs(sti, stj):
    person = deque([(sti, stj, 1)])
    while person:
        i, j, cnt = person.popleft()
        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                return cnt
            if building[ni][nj] == '.':
                building[ni][nj] = ','
                person.append((ni, nj, cnt + 1))

        while fire:
            fi, fj = fire.popleft()
            for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nfi = fi + di
                nfj = fj + dj
                if 0 <= nfi < n and 0 <= nfj < m:
                    if building[nfi][nfj] == '.' or building[nfi][nfj] == ',':
                        building[nfi][nfj] = '*'
                        fire.append((nfi, nfj))

    return 'IMPOSSIBLE'

for _ in range(int(input())):
    m, n = map(int, input().split())
    building = [list(input()) for _ in range(n)]
    fire = deque()
    for i in range(n):
        for j in range(m):
            if building[i][j] == '@':
                sti, stj = i, j
                building[sti][stj] = ','

            if building[i][j] == '*':
                fire.append((i, j))

    print(bfs(sti, stj))