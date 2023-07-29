
def DFS(st):
    for k in arr[st]:
        if not visited[k]:
            visited[k] = visited[st] + 1
            DFS(k)

n = int(input())
x, y = map(int, input().split())
arr = [[] for _ in range(n+1)]
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [0 for _ in range(n+1)]
DFS(x)
print(visited[y] if visited[y] > 0 else -1)