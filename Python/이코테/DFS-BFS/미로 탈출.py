from collections import deque

def bfs(sti, stj):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    visited[sti][stj] = 1
    q.append((sti, stj))
    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and miro[ni][nj] == 1:
                q.append((ni, nj))
                visited[ni][nj] += visited[i][j] + 1
    return(visited[n-1][m-1])

n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]
print(bfs(0, 0))

# from collections import deque
#
# # N, M을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())
# # 2차원 리스트의 맵 정보 입력받기
# graph = [list(map(int, input())) for _ in range(n)]
#
# # 이동할 네 방향 정의(상, 하, 좌, 우)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# # BFS 코드 구현
# def bfs(x, y):
#     # 큐(Queue) 구현을 위해 deque 라이브러리 사용
#     queue = deque() # [x, y]
#     queue.append((x, y))
#     # 큐가 빌 때까지 반복
#     print(queue)
#     while queue:
#         x, y = queue.popleft()
#         # 현재 위치에서 네 방향으로 위치 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 미로 찾기 공간에서 벗어난 경우 무시
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             #벽인 경우 무시
#             if graph[nx][ny] == 0:
#                 continue
#             # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
#     # 가장 오른쪽 아래까지의 최단 거리 반환
#     return graph[n-1][m-1]
#
# print(bfs(0,0))

"""
5 6
101010
111111
000001
111111
111111
"""