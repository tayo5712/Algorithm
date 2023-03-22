# 내풀이
def dfs(a, b):
    visited[a][b] = 1
    for di, dj in [[0, 1], [1, 0], [-1, 0], [0 ,-1]]:
        ni = a + di
        nj = b + dj
        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and mapp[ni][nj] == 0:
            dfs(ni, nj)

n, m = map(int, input().split())
mapp = [list(map(int, input())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if mapp[i][j] == 0 and not visited[i][j]:
            dfs(i, j)
            cnt += 1
print(cnt)

# n, m = map(int, input().split())
#
# graph = [list(map(int, input())) for _ in range(n)]
#
# # DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
# def dfs(x, y):
#     # 주어진 범위를 벗어나는 경우에는 즉시 종료
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     # 현재 아직 방문하지 않았다면
#     if graph[x][y] == 0:
#         # 해당 노드 방문 처리
#         graph[x][y] = 1
#         # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False
#
# result = 0
# for i in range(n):
#     for j in range(m):
#         # 현재 위치에서 DFS 수행
#         if dfs(i, j) == True:
#             result += 1
# print(result)