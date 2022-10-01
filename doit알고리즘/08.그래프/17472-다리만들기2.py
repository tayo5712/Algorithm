from collections import deque
from heapq import heappush, heappop

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(a, b):    # 유니온 파인드
    a = find_set(a)
    b = find_set(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def make_bridge(b):
    start = world[b[0]][b[1]]
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        i = b[0]
        j = b[1]
        bridge_len = 0
        while True:     # 한 방향으로 가면서 다리 만들기
            ni = i + di
            nj = j + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m or world[ni][nj] == start:    # 범위 밖이고 자기 다리가 같은 섬끼리 연결 되면 break
                break
            if world[ni][nj] and bridge_len == 1:   # 다른 섬에 도착했는데 다리 길이가 1 이면 break
                break
            if world[ni][nj] and bridge_len > 1:    # 다른 섬에 도착했는데 다리 길이가 2 이상이면 start섬과 end섬의 최소 다리 길이를 업데이트
                end = world[ni][nj]
                dist[start][end] = min(dist[start][end], bridge_len)
                break

            i = ni
            j = nj
            bridge_len += 1


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
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                if world[ni][nj] == 1:
                    world[ni][nj] = group
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                if not world[ni][nj]:       # 섬의 테두리 위치
                    edge.add((a, b))

n, m = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(n)]

edge = set()    # 섬의 테두리 위치 담을 변수
group = 1
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if world[i][j] == 1 and not visited[i][j]:  # 섬 그룹화
            bfs_group(i, j)
            group += 1

edge = list(edge)
g_n = group - 1     # 섬의 개수

dist = [[100] * (g_n+1) for _ in range(g_n+1)]      # 섬 사이의 거리를 담을 2차원 배열

for i in edge:  # 테두리에서 다리 만들기
    make_bridge(i)

heap = []
for i in range(1, g_n+1):
    for j in range(1, g_n+1):
        if dist[i][j] != 100:
            heappush(heap, (dist[i][j], i, j))      # 섬과 섬 사이의 거리 정보가 있으면 heap에 push

parent = list(range(g_n+1))
cnt = 0
total_bridge_len = 0
check = False

while heap:     # kruskal
    bridge_len, start, end = heappop(heap)
    if find_set(start) != find_set(end):
        union(start, end)
        cnt += 1
        total_bridge_len += bridge_len
    if cnt == g_n - 1:   # 섬의 개수 - 1 만큼 다리가 있으면 종료
        check = True
        break

if check:   # 섬의 개수 - 1만큼 다리가 있으면 총 다리의 길이 출력
    print(total_bridge_len)
else:
    print(-1)
