from collections import deque
from itertools import combinations

def is_connect(r, c):   # 7명이 연결되어 있는지? + 이다솜 파가 4명이상 인지?
    q = deque()
    q.append((r, c))
    visited[r][c] = 0
    cnt = 1
    som = 0
    while q:
        r, c = q.popleft()
        if school[r][c] == 'S':
            som += 1
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc]:
                visited[nr][nc] = 0
                q.append((nr, nc))
                cnt += 1

    if cnt == 7 and som >= 4:   # 7명이 이어져있고 이다솜파가 4명 이상이면
        return True
    return False

n = 5
school = [input() for _ in range(n)]
answer = 0
for com in combinations(list(range(25)), 7):    # 25명에서 7명 뽑기
    visited = [[0] * n for _ in range(n)]
    for num in com:
        r, c = num // 5, num % 5    # 번호에서 열의 길이로 나누면 행의 번호가 되고 열의 길이로 나눈 나머지는 열의 번호가 된다.
        visited[r][c] = 1
    if is_connect(r, c):    # 7명 연결되있는지 확인
        answer += 1
print(answer)

#
#
# 인접하는 애들 계속 넣어서 dfs 돌린건데 되게 오래걸림
#
# school = [input() for _ in range(5)]
# n = 5
# result_set = set()
#
# def backtrack(arr, S, Y):
#     if Y > 3:
#         return
#     if len(arr) == 7:
#         arr.sort()
#         result_set.add(tuple(arr))
#     else:
#         for a, b in arr:
#             for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                 dx = a + di
#                 dy = b + dj
#                 if 0 <= dx < n and 0 <= dy < n and (dx, dy) not in arr:
#                     if school[dx][dy] == 'S':
#                         backtrack(arr+[(dx, dy)], S+1, Y)
#                     else:
#                         backtrack(arr+[(dx, dy)], S, Y+1)
#
# for i in range(n):
#     for j in range(n):
#         if school[i][j] == 'S':
#             backtrack([(i, j)], 1, 0)
#
# print(len(result_set))
#

