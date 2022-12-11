from collections import deque

def bfs(sti, stj):
    cnt = 1
    visited[sti][stj] = 1
    q = deque()
    q.append((sti, stj))
    while q:
        i, j = q.popleft()
        grouping[i][j] = group  # 그룹 숫자 표시
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and mapp[ni][nj] == 0:
                cnt += 1
                visited[ni][nj] = 1
                q.append((ni, nj))
    group_dict[group] = cnt     # 해당 그룹의 수를 저장

def check_group(ci, cj):
    my_group = set()    # 현재 벽위치에서 상하좌우에 인접한 그룹 확인 (중복 제거)
    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ni = i + di
        nj = j + dj
        if 0 <= ni < n and 0 <= nj < m and grouping[ni][nj]:
            my_group.add(grouping[ni][nj])
    answer = 1  # 벽 자기 자신 포함
    for mg in my_group:     # 자기칸과 인접한 그룹의 칸의 개수를 더해준다.
        answer += group_dict[mg]
        result[ci][cj] = answer % 10    # 문제에서 10으로 나눈 나머지를 출력


n, m = map(int, input().split())
mapp = [list(map(int, input())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]     # 방문 확인
grouping = [[0 for _ in range(m)] for _ in range(n)]    # 그룹핑
result = [[0 for _ in range(m)] for _ in range(n)]      # 결과 값 저장
group_dict = {}     # 그룹의 수를 저장할 딕셔너리

group = 1   # 그룹 구분할 숫자
for i in range(n):
    for j in range(m):
        if mapp[i][j] == 0 and not visited[i][j]:   # 0이고 아직 방문하지 않았으면
            bfs(i, j)
            group += 1  # 그룹 갱신

for i in range(n):
    for j in range(m):
        if mapp[i][j] == 1:
            check_group(i, j)   # 벽 상하좌우의 그룹 확인

for k in range(n):
    for v in range(m):
        print(result[k][v], end="")
    print()
