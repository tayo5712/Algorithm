
def dfs(x):
    visited[x] = 1
    for nx in path[x]:
        if left[nx] == -1 or (not visited[left[nx]] and dfs(left[nx])):
            right[x] = nx
            left[nx] = x
            return True
    return False

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dr = [1, 1]
dc = [1, -1]
id = [[[-1] * n for _ in range(n)] for _ in range(2)]
count = [0, 0]
for dir in range(2):
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1 and id[dir][r][c] == -1:
                nr, nc = r, c
                while 0 <= nr < n and 0 <= nc < n:
                    if board[nr][nc] == 1:
                        id[dir][nr][nc] = count[dir]
                    nr += dr[dir]
                    nc += dc[dir]
                count[dir] += 1

a = count[0]
b = count[1]
path = [[] for _ in range(a)]
for i in range(n):
    for j in range(n):
        if board[i][j]:
            path[id[0][i][j]].append(id[1][i][j])

right = [-1] * a
left = [-1] * b
answer = 0
print(path)
for i in range(a):
    if right[i] == -1:
        visited = [0] * a
        if dfs(i):
            answer += 1
print(right)
print(left)
print(answer)