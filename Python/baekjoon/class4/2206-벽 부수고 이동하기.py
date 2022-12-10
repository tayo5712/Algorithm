from collections import deque

def bfs(i, j):
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]   # 3차원 배열 visited[x][y][z]
                                                                # z=0이면 벽을 안뚫고 지나갔을 때
                                                                # z=1이면 벽을 한 번 뚫고 지나갔을 때
    visited[i][j][0] = 1
    q = deque()
    q.append((i, j, 0))
    while q:
        i, j, k = q.popleft()
        if i == n-1 and j == m-1:
            return visited[i][j][k]

        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m:

                if mapp[ni][nj] == 0 and not visited[ni][nj][k]:    # 다음 위치가 길이면 넘겨준다.
                    visited[ni][nj][k] = visited[i][j][k] + 1
                    q.append((ni, nj, k))

                elif mapp[ni][nj] == 1 and k == 0:   # 다음 위치가 벽이고 한 번도 뚫고 지나 간 적이 없을 때
                    visited[ni][nj][k+1] = visited[i][j][k] + 1     # 벽을 뚫고 지나간 경로로 변경한다.
                    q.append((ni, nj, k+1))
    return -1

n, m = map(int, input().split())
mapp = [list(map(int, input())) for _ in range(n)]
print(bfs(0, 0))