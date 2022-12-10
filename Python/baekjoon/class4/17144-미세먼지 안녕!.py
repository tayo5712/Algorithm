r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
air_cleaner = []

for i in range(r):
    for j in range(c):
        if room[i][j] == -1:
            air_cleaner.append([i, j])

while t > 0:
    # 먼지 확산
    temp = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] // 5 >= 1:
                cnt = 0
                for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                   ni = i + di
                   nj = j + dj
                   if 0 <= ni < r and 0 <= nj < c and room[ni][nj] != -1:
                       temp[ni][nj] += room[i][j] // 5
                       cnt += 1
                room[i][j] -= (room[i][j] // 5) * cnt

    for i in range(r):
        for j in range(c):
            room[i][j] += temp[i][j]

    # 공기청정기 윗부분
    before = room[air_cleaner[0][0]][1]
    room[air_cleaner[0][0]][1] = 0
    a, b = air_cleaner[0][0], 1
    for di, dj in [[0, 1], [-1, 0], [0, -1], [1, 0]]:
        while True:
            ni = a + di
            nj = b + dj
            if ni < 0 or ni >= r or nj >= c or nj < 0 or room[ni][nj] == -1:
                break
            else:
                after = room[ni][nj]
                room[ni][nj] = before
                before = after
                a = ni
                b = nj

    # 공기청정기 아래부분
    before = room[air_cleaner[1][0]][1]
    room[air_cleaner[1][0]][1] = 0
    a, b = air_cleaner[1][0], 1
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        while True:
            ni = a + di
            nj = b + dj
            if ni < 0 or ni >= r or nj >= c or nj < 0 or room[ni][nj] == -1:
                break
            else:
                after = room[ni][nj]
                room[ni][nj] = before
                before = after
                a = ni
                b = nj
    t -= 1

sum = 0
for i in range(r):
    for j in range(c):
       if room[i][j] > 0:
           sum += room[i][j]

print(sum)
