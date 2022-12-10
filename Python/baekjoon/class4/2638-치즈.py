from collections import deque

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    q = deque()
    q.append((0, 0))    # 0,0 에서 시작해서 bfs 돌려서 만나면 공기에 노출된 것으로 처리
    visited = [[0 for _ in range(m)] for _ in range(n)]
    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if paper[ni][nj] == 1:  # 치즈인데
                    if visited[ni][nj] != 2:    # 공기를 2변이상 접하지 않은 경우
                        visited[ni][nj] += 1    # 공기를 1변 접한것으로 1더해주기
                        if visited[ni][nj] == 2:    # 공기를 2변 접했으면, 나중에 삭제하기 위해서 리스트에 좌표 넣어줌
                            del_q.append((ni, nj))
                else:   # 공기 이면
                    if not visited[ni][nj]: # 공기 방문하지 않았다면
                        visited[ni][nj] = 1 # 방문 처리후 큐에 넣어줌
                        q.append((ni, nj))
cnt = 0
while True:
    del_q = []  # 2변이 노출된 치즈 좌표 넣을 리스트
    bfs()
    if del_q:   # 공기에 2변이 노출된 치즈가 있으면 0으로 만들어주고 cnt 1더해주기
        for di, dj in del_q:
            paper[di][dj] = 0
        cnt += 1
    else:
        break
print(cnt)

