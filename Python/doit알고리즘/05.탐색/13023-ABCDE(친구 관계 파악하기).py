import sys
input = sys.stdin.readline

def dfs(now, depth):
    global arrive
    if depth == 5:
        arrive = True           # 도착 true
        return
    visited[now] = 1
    for i in graph[now]:
        if not visited[i]:
            dfs(i, depth+1)     # 깊이를 1씩 더해서 넘겨준다.
    visited[now] = 0            # 모든 노드에서 dfs를 해야해서 visited 열어줘야함

v, e = map(int, input().split())
visited = [0] * v
graph = [[] for _ in range(v)]
arrive = False          # 도착 확인용

for _ in range(e):
    st, ed = map(int, input().split())
    graph[st].append(ed)
    graph[ed].append(st)

for i in range(v):
    dfs(i, 1)
    if arrive:          # 깊이가 5인게 있으면
        break           # 즉시 종료

if arrive:              # 깊이가 5인게 있으면 1 출력
    print(1)
else:
    print(0)