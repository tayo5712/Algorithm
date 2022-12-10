from collections import deque

def bfs(start):
    visited = [-1] * 100002 # 목표 좌표보다 1보다 큰위치로 와서 -1을 해서 목표로 가는 것 말고는 목표를 넘어갈 필요가 없다.
    visited[start] = 0
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        if now == k:
            return visited[now]

        next = now * 2  # 텔레포트는 시간이 안드니깐 먼저 해줘야 한다.
        if 0 <= next <= 100001 and visited[next] == -1:
            visited[next] = visited[now]    # 텔레포트는 이동시간 그대로
            q.append(next)

        for dx in (-1, 1):
            next = now + dx
            if 0 <= next <= 100001 and visited[next] == -1:
                visited[next] = visited[now] + 1    # 걷는 거는 1초 추가
                q.append(next)

n, k = map(int, input().split())
print(bfs(n))