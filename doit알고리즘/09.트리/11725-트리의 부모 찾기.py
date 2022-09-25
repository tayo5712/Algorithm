import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())

visited = [0] * (n+1)
answer = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(1, n):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(v):
    visited[v] = 1
    for k in graph[v]:
        if not visited[k]:
            visited[k] = 1
            answer[k] = v       # 루트 노드인 1을 시작점으로 dfs 했기 때문에 dfs 할 수록 밑으로 내려감
            dfs(k)

dfs(1)

for i in range(2, n+1):
    print(answer[i])