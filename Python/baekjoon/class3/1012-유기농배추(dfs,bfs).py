
# bfs 풀이 ( 메모리 : 115248KB, 시간 : 164ms)
# def bfs(st):
#     global cnt
#     while st:
#         i, j = st.pop(0)        # 앞에서 부터 1의 좌표 값 뽑아내기
#         if not world[i][j]:     # 1의 좌표가 있던 곳이 1이 아니면 continue
#             continue
#         else:                   # 1의 좌표가 있던 곳이 1이면
#             q = []              # bfs할 q생성
#             k.append((i, j))
#             cnt += 1            # while문 들어가기전에 cnt += 1 (그 범위 전부 0으로 만들꺼라서 한 범위당 1 추가)
#             while k:
#                 i, j = q.pop(0)
#                 world[i][j] = 0 # 1 이였던 곳 0으로 바꿔버림
#                 for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
#                     ni = i + di
#                     nj = j + dj
#                     if 0 <= ni < n and 0 <= nj < m and world[ni][nj]:
#                         world[ni][nj] = 0   # 1이 있는 좌표랑 상하좌우로 이어져 있는 1은 전부 0으로 바꿈
#                         q.append((ni, nj))
#
# t = int(input())
# for _ in range(t):
#     n, m, k = map(int, input().split())
#     world = [[0] * m for _ in range(n)]
#     cnt = 0
#     st = []
#     for _ in range(k):
#         a, b = map(int, input().split())
#         world[a][b] = 1
#         st.append((a, b))          # 1의 좌표를 st에 저장
#
#     bfs(st)
#     print(cnt)

# dfs 풀이 (메모리 : 184460KB, 시간 : 264ms)
import sys
input = sys.stdin.readline

def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= m or not world[i][j]:  # i, j 값이 범위 밖이거나 1이 아니면 continue
        return False
    world[i][j] = 0     # 1인 자리 0으로 지워나감 (방문표시)
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:   # 상하좌우 dfs 재귀 확인
        dfs(i+di, j+dj)
    return True     # 전부 다 돌고나서 True 반환해줘서 cnt +=1 해줌

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    world = [[0] * m for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        world[a][b] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j):       # 해당 1 좌표에대한 dfs를 돌고 True가 반환되면 cnt += 1
                cnt += 1
    print(cnt)
























