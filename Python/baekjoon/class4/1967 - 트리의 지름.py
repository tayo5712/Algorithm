import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(i):
    for ni, w in graph[i]:
        if visited[ni] == -1:
            visited[ni] = visited[i] + w
            dfs(ni)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    st, ed, w = map(int, input().split())
    graph[st].append((ed, w))
    graph[ed].append((st, w))

visited = [-1] * (n+1)
visited[1] = 0
dfs(1)

new_st = visited.index(max(visited))
visited = [-1] * (n+1)
visited[new_st] = 0
dfs(new_st)

print(max(visited))