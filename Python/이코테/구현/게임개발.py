n, m= map(int, input().split())
r, c, direction = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]
visited[r][c] = 1 # 시작 위치 방문처리

dr = [1, 0, -1, 0]  # 북, 서, 남, 동
dc = [0, -1, 0, 1]

turn_time = 0   # 회전 횟수
cnt = 1 # 방문한 칸 수

def turn_left():    # 왼쪽으로 회전 하는 함수
    global direction
    global turn_time
    turn_time += 1
    direction = (direction + 1) % 4

while True:
    turn_left()
    nr, nc = r + dr[direction], c + dc[direction]
    if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and not mapp[nr][nc]:    # 칸 밖으로 나가지 않고, 가보지 않고, 바다가 아닐 경우 이동
        r, c = nr, nc
        cnt += 1
        visited[nr][nc] = 1
        turn_time = 0   # 이동 시 회전 횟수 초기화

    if turn_time == 4:  # 4방향 다 회전했는데도 갈 곳이 없으면
        r, c = r - dr[direction], c - dc[direction] # 뒤로 방향 유지한 채 후진
        if mapp[r][c]:  # 후진한 곳이 바다이면 while문 break
            break
        turn_time = 0   # 아니면 회전 횟수 초기화
print(cnt)