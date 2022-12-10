from collections import deque

def bfs(N):
    q = deque()
    q.append(N)
    visited = [[-1, 0] for _ in range(100001)]
    visited[N][0] = 0
    visited[N][1] = 1

    while q:
        now = q.popleft()

        for next in (now-1, now+1, now*2):
            if 0 <= next <= 100000:
                if visited[next][0] == -1:  # 처음 도착
                    visited[next][0] = visited[now][0] + 1  # 걸린 시간
                    visited[next][1] = visited[now][1]  # 경우의 수
                    q.append(next)

                elif visited[next][0] == visited[now][0] + 1:   # 처음 도착은 아니지만 최단 시간이라면
                    visited[next][1] += visited[now][1]  # 경우의 수 갱신

    print(visited[K][0])
    print(visited[K][1])

N, K = map(int, input().split())
bfs(N)

