from collections import deque

def make_bridge(b):
    global minV
    start = world[b[0]][b[1]]
    visited = [[-1] * n for _ in range(n)]
    visited[b[0]][b[1]] = 0
    q = deque()
    q.append(b)
    while q:
        a, b = q.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni = a + di
            nj = b + dj
            if 0 <= ni < n and 0 <= nj < n:     # 범위 안이면
                if world[ni][nj] != start and world[ni][nj]:    # 같은 섬이 아니고 다른 섬이면
                    minV = min(minV, visited[a][b])             # 최소값 비교
                    return
                if not world[ni][nj] and visited[ni][nj] == -1:     # 바다이고 방문하지 않았으면
                    visited[ni][nj] = visited[a][b] + 1             # 거리를 1씩 더해서 나아간다.
                    q.append((ni, nj))

def bfs_group(a, b):    # 섬 그룹화 하기
    q = deque()
    q.append((a, b))
    world[a][b] = group
    visited[a][b] = 1
    while q:
        a, b = q.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni = a + di
            nj = b + dj
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if world[ni][nj] == 1:
                    world[ni][nj] = group
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                if not world[ni][nj]:       # 섬의 테두리 위치
                    edge.add((a, b))

n = int(input())
world = [list(map(int, input().split())) for _ in range(n)]

edge = set()    # 섬의 테두리 위치 담을 변수
group = 1
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if world[i][j] == 1 and not visited[i][j]:  # 섬 그룹화
            bfs_group(i, j)
            group += 1

edge = list(edge)
minV = 10000
for i in edge:  # 테두리에서 다리 만들기
    make_bridge(i)

print(minV)
