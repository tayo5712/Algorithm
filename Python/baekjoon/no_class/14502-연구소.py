import copy
import sys

def bfs(arr):
    global maxV
    arr2 = copy.deepcopy(arr)           # 지도에 직접 표시를 할 것이기 때문에 원본을 deepcopy해서 여러 개의 경우의 수 체크
    q = []
    for i in range(n):
        for j in range(m):
            if arr2[i][j] == 2:         # 값이 2인곳에서 bfs 시작
                q.append((i, j))
    while q:
        i, j = q.pop(0)
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m and arr2[ni][nj] == 0:
                q.append((ni, nj))
                arr2[ni][nj] = 2

    cnt = 0
    for i in range(n):                  # 안전지대(0)의 개수가 최대일 때를 구하기
        for j in range(m):
            if arr2[i][j] == 0:
                cnt += 1

    if cnt > maxV:
        maxV = cnt


def wall(cnt):   # 벽 3개 위치 정하기
    if cnt == 3:
        bfs(arr)
        return
    for a in range(n):
        for b in range(m):
            if arr[a][b] == 0:
                arr[a][b] = 1
                wall(cnt + 1)
                arr[a][b] = 0


n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
maxV = 0

wall(0)
print(maxV)