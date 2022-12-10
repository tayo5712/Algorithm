from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    global person, fire
    while person:
        temp = deque()
        x, y = person.popleft()
        if (x == h - 1 or y == w - 1 or x == 0 or y == 0) and building[x][y] != "":
            return building[x][y]
        for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < h and 0 <= ny < w and building[nx][ny] == ".":
                building[nx][ny] = building[x][y] + 1
                temp.append([nx, ny])

        person = temp
        temp = deque()
        while fire:
            x, y = fire.popleft()
            for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < h and 0 <= ny < w and visit[nx][ny] == 0 and building[nx][ny] != "#":
                    building[nx][ny] = ""
                    visit[nx][ny] = 1
                    temp.append([nx, ny])
        fire = temp

for _ in range(int(input())):
    w, h = map(int, input().split())
    person, fire = deque(), deque()
    visit = [[0] * w for i in range(h)]
    building = [list(input()) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if building[i][j] == "@":
                building[i][j] = 1
                person.append((i, j))
            elif building[i][j] == "*":
                fire.append((i, j))
                visit[i][j] = 1
    result = bfs()
    print(result if result != None else "IMPOSSIBLE")