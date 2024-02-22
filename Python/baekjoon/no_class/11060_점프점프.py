from collections import deque

n = int(input())
arr = list(map(int, input().split()))

def bfs():
    q = deque()
    q.append((0, 0))
    visited = [0] * n
    visited[0] = 1
    while q:
        pos, cnt = q.popleft()
        if pos == n - 1:
            return cnt
        for i in range(1, arr[pos] + 1):
            next = pos + i
            if next < n and not visited[next]:
                q.append((next, cnt + 1))
                visited[next] = 1
    return -1

print(bfs())
