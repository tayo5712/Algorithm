from collections import deque

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
room_cnt = 0
biggest_room = 0
remove_biggest_room = 0

dr = [0, -1, 0, 1]  # 서북동서
dc = [-1, 0, 1, 0]
room_kind = 1
area_dict = dict()
def bfs(str, stc, rn):
    q = deque([(str, stc)])
    area = 1
    while q:
        cr, cc = q.popleft()
        bit = arr[cr][cc]
        for i in range(4):  # 막혀 있지 않을 때
            if bit | 1 << i != bit:
                nr = cr + dr[i]
                nc = cc + dc[i]
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                    visited[nr][nc] = rn
                    area += 1
                    q.append((nr, nc))
    area_dict[rn] = area
    return area


visited = [[0 for _  in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            room_cnt += 1
            visited[i][j] = room_kind
            biggest_room = max(biggest_room, bfs(i, j, room_kind))
            room_kind += 1

for i in range(n): # 이웃한 영역 끼리의 합의 최대값
    for j in range(m):
        for k in range(4):
            if arr[i][j] | 1 << k == arr[i][j]:
                if 0 <= i + dr[k] < n and 0 <= j + dc[k] < m and visited[i][j] != visited[i + dr[k]][j + dc[k]]:
                    remove_biggest_room = max(remove_biggest_room, area_dict[visited[i][j]] + area_dict[visited[i + dr[k]][j + dc[k]]])

print(room_cnt)
print(biggest_room)
print(remove_biggest_room)
