from collections import deque

def bfs(shark_x, shark_y):
    visited = [[-1] * n for _ in range(n)]
    visited[shark_x][shark_y] = 0
    q = deque([(shark_x, shark_y)])
    fish = []
    min_dist = 10000
    while q:
        i, j = q.popleft()
        for di, dj in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == -1 and sea[ni][nj] <= shark_size:
                visited[ni][nj] = visited[i][j] + 1
                if 0 < sea[ni][nj] < shark_size:
                    min_dist = visited[ni][nj]
                    fish.append((visited[ni][nj], ni, nj))
                if visited[ni][nj] <= min_dist:
                    q.append((ni, nj))

    if fish:
        fish.sort()
        return fish[0]
    else:
        return -1

shark_x, shark_y =0, 0
shark_size = 2
eat_cnt = 0
fish_cnt = 0
n = int(input())
sea = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if 0 < sea[i][j] <= 6:
            fish_cnt += 1
        elif sea[i][j] == 9:
            sea[i][j] = 0
            shark_x, shark_y = i, j

time = 0
while fish_cnt:
    result = bfs(shark_x, shark_y)
    if result == -1:
        break
    time += result[0]
    shark_x, shark_y = result[1], result[2]
    sea[result[1]][result[2]] = 0
    fish_cnt -= 1
    eat_cnt += 1
    if eat_cnt == shark_size:
        shark_size += 1
        eat_cnt = 0

print(time)

