# dfs로 풀면 됨

def dfs(st):
    global cnt
    visited[st] = 1
    for i in graph[st]:
        if visited[i]==0:
            dfs(i)
            cnt += 1

v = int(input())
e = int(input())
graph = [[] * v for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0] * (v+1)

dfs(1)
print(cnt)





