from collections import deque

def bfs(a):
    q = deque([a])
    visited = [-1] * (k + 1)
    visited[a] = 0
    while q:
        num = q.popleft()
        if num == k:
            return visited[num]
        for oper in (1, num):
            next = num + oper
            if next <= k and visited[next] == -1:
                visited[next] = visited[num] + 1
                q.append(next)
    return -1

a, k = map(int, input().split())
print(bfs(a))
