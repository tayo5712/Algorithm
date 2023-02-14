# 비어있는 칸 '.', 소나기 '*', 강 'X', 집 'H', 세차장 'W'
from collections import deque


def bfs(Wr, Wc):
    Wq = deque()
    W_visited = [[-1 for _ in range(c)] for _ in range(r)]  # visited 방문처리겸 이동 시간 확인
    W_visited[Wr][Wc] = 0   # 세차장 위치 방문 처리 및 초기 시간 0 설정
    Wq.append((Wr, Wc))
    cnt = 0     # 경과 시간
    rain()      # 이동 전 소나기 내리기

    while Wq:
        wr, wc = Wq.popleft()
        if cnt != W_visited[wr][wc]:    # 시간이 증가했으면(한 사이클 돌았으면) 소나기 확산
            rain()
        cnt = W_visited[wr][wc]

        for di, dj in ([1, 0], [0, 1], [-1, 0], [0, -1]):
            nr, nc = wr + di, wc + dj
            if 0 <= nr < r and 0 <= nc < c and W_visited[nr][nc] == -1:
                if mapp[nr][nc] == '.':     # 이동했으면 현재 위치에서의 경과시간에 1을 더하고 다음 위치 큐에 추가
                    W_visited[nr][nc] = W_visited[wr][wc] + 1
                    Wq.append((nr, nc))
                if mapp[nr][nc] == 'H':     # 집에 도착했으면 전 위치에서의 경과시간에 1을 더해 반환
                    return W_visited[wr][wc] + 1

    return "FAIL"   # 집에 도착하지 않았는데 더 이상 이동할 곳이 없으면 FAIL

def rain():
    global Sq   # 소나기 위치 가져오기
    tmp = deque()   # 다음 소나기 확산 위치 저장하는 곳
    while Sq:
        sr, sc = Sq.popleft()
        for di, dj in ([1, 0], [0, 1], [-1, 0], [0, -1]):
            nr, nc = sr + di, sc + dj
            if 0 <= nr < r and 0 <= nc < c and mapp[nr][nc] == ".":
                mapp[nr][nc] = '*'
                tmp.append((nr, nc))
    Sq = tmp    # 다음 소나기 확산 위치를 현재 소나기 위치로 바꿔주고 끝내기
    return

r, c = map(int, input().split())
mapp = [list(input()) for _ in range(r)]
Wr, Wc = 0, 0
Sq = deque()    # 소나기 좌표 deque
for i in range(r):
    for j in range(c):
        if mapp[i][j] == 'W':   # 세차장 좌표
            Wr = i
            Wc = j

        if mapp[i][j] == '*':   # 소나기 좌표
            Sq.append((i, j))

print(bfs(Wr, Wc))
