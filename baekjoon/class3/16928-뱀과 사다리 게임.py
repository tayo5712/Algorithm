from collections import deque

def bfs(start):
    q = deque()
    q.append((start, 0))    # 1부터 시작, 주사위 굴린 횟수
    visited = [0] * 101
    visited[start] = 1
    while q:
        now, cnt = q.popleft()
        if now == 100:      # bfs는 먼저 도달한 값이 최소값이다.
            return cnt

        for dice in range(1, 7):        # 주사위 1~6 굴림
            next = now + dice
            if next in warp:            # 만약 다음 이동해야할 칸에 뱀이나 사다리가 있으면 그곳으로 이동
                next = warp[next]
            if next <= 100 and not visited[next]:       # 이동하는 칸이 100칸 이하이고 방문한 적이 없으면
                visited[next] = 1           # 방문 처리 후 굴린 횟수에 1을 더해 큐에 삽입
                q.append((next, cnt+1))

n, m = map(int, input().split())
warp = {}   # 뱀과 사다리의 정보를 담을 딕셔너리 (키값은 시작점, 밸류값은 도착점)
for _ in range(n+m):
    st, ed = map(int, input().split())
    warp[st] = ed

print(bfs(1))