def bfs(n, m, dir):
    global cnt
    flag = 0
    while True:
        if mapp[n][m] == 0:
            mapp[n][m] = 2
            cnt += 1
        dir = (dir+3) % 4
        nr = n + dr[dir]
        nc = m + dc[dir]
        if mapp[nr][nc] == 0:
            mapp[nr][nc] = 2
            cnt += 1
            n = nr
            m = nc
            flag = 0
        else:
            flag += 1
        if flag == 4:
            nr = n - dr[dir]
            nc = m - dc[dir]
            if mapp[nr][nc] == 1:
                break
            else:
                n = nr
                m = nc
                flag = 0

n, m = map(int, input().split())
stn, stm, dir = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
bfs(stn, stm, dir)
print(cnt)
