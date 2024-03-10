from collections import deque

def bfs():
    if subin > sister:
        return subin - sister, [int(x) for x in range(subin, sister - 1, -1)]
    q = deque()
    q.append((subin, 0, []))
    visited = [0] * 100001
    visited[subin] = 1
    while q:
        now_s, cnt, move = q.popleft()

        if now_s == sister:
            return cnt, move + [now_s]

        for next_s in [now_s + 1, now_s - 1, now_s * 2]:
            if 0 <= next_s < 100001 and not visited[next_s]:
                visited[next_s] = 1
                q.append((next_s, cnt + 1, move + [now_s]))

subin, sister = map(int, input().split())
cnt, move = bfs()
print(cnt)
print(*move)
