from collections import deque
import sys
input = sys.stdin.readline

def bfs(a):
    visited = [0] * 10000
    visited[a] = 1
    q = deque()
    q.append((a, ''))
    while q:
        a, oper = q.popleft()
        if a == b:
            return oper

        na = (a * 2) % 10000
        if not visited[na]:
            q.append((na, oper+'D'))
            visited[na] = 1

        na = (a - 1) % 10000
        if not visited[na]:
            q.append((na, oper+'S'))
            visited[na] = 1

        na = (a % 1000) * 10 + a // 1000
        if not visited[na]:
            q.append((na, oper+'L'))
            visited[na] = 1

        na = a // 10 + (a % 10) * 1000
        if not visited[na]:
            q.append((na, oper+'R'))
            visited[na] = 1

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(bfs(a))