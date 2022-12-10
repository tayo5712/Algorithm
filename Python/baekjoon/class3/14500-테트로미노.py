def dfs(i, j, idx, sumV, visited):  # 행, 열, 깊이, 합계, 방문
    global answer
    if answer >= sumV + maxV * (3-idx):     # 현재 까지 구한 테트로미노의 최대값 보다 현재 확인 중인 테트로미노의 합 + 남은 깊이*최대칸값 이 작거나 같으면 볼 필요 없으므로 return
        return
    if idx == 3:    # 깊이가 3이면 블록 4칸을 다 본것이므로 그 값을 테트로미노 최대값에 넣어준다. (위에서 작은 값은 다 걸러져서 바로 넣으면 됨)
        answer = sumV
        return
    else:
        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                if idx == 1:       # 블록을 2개까지 보면은 'ㅗ'모양을 만들기 위해서 다음칸의 값만 합해주고 가지 않는다. 다시 제자리에서 dfs
                    visited[ni][nj] = 1
                    dfs(i, j, idx+1, sumV + arr[ni][nj], visited)
                    visited[ni][nj] = 0
                visited[ni][nj] = 1     # 블록을 4개까지 볼때까지 다음 칸에서 dfs 진행
                dfs(ni, nj, idx+1, sumV + arr[ni][nj], visited)
                visited[ni][nj] = 0     # 갔다와서 방문 취소

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
maxV = (max(map(max, arr)))     # 모든 칸 중 가장 높은 값을 찾아논다.
visited = [[0 for _ in range(m)] for _ in range(n)]     # 방문 처리할 배열

answer = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = 1   # 모든 칸을 돌면서 DFS 실행
        dfs(i, j, 0, arr[i][j], visited)
        visited[i][j] = 0   # 갔다와서 방문 처리 취소

print(answer)

# from itertools import combinations
# from collections import deque
#
# def is_connect(r, c):
#     global maxV
#     q = deque()
#     q.append((r, c))
#     visited[r][c] = 0
#     cnt = 1
#     sumV = arr[r][c]
#     while q:
#         r, c = q.popleft()
#         for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
#             nr = r + dr
#             nc = c + dc
#             if 0 <= nr < n and 0 <= nc < m and visited[nr][nc]:
#                 visited[nr][nc] = 0
#                 sumV += arr[nr][nc]
#                 cnt += 1
#                 q.append((nr, nc))
#
#     if cnt == 4:
#         maxV = max(maxV, sumV)
#
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# maxV = 0
#
# for value in combinations([i for i in range(n*m)], 4):
#     visited = [[0] * m for _ in range(n)]
#     for block in value:
#         r, c = block // m, block % m
#         visited[r][c] = 1
#     is_connect(r, c)
#
# print(maxV)