
def DFS(st, visited, L):
    for k in arr[st]:
        if not visited[k]:
            if k == y:
                return L + 1;
            else:
                visited[k] = 1
                result = DFS(k, visited, L + 1)
                if result != -1:
                    return result
    return -1

n = int(input())
x, y = map(int, input().split())
arr = [[] for _ in range(n+1)]
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [0 for _ in range(n+1)]
visited[x] = 1
print(DFS(x, visited, 0))