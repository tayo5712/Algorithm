
# 플로이드 워셜

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1

for i in arr:
    print(*i)

# dfs
#
# def dfs(st, visited):
#     for i in graph[st]:
#         if not visited[i]:
#             visited[i] = 1
#             dfs(i, visited)
#
# n = int(input())
#
# graph = [[] for _ in range(n)]
#
# for i in range(n):
#     arr = list(map(int, input().split()))
#     for j in range(n):
#         if arr[j]:
#             graph[i].append(j)
#
# for i in range(n):
#     visited = [0] * n
#     dfs(i, visited)
#     print(*visited)
