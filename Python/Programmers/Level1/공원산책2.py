
from collections import deque

direction = {"E": [0, 1], "W": [0, -1], "S": [1, 0], "N": [-1, 0]}
def solution(park, routes):
    n = len(park)
    m = len(park[0])

    def move(str, stc):
        for w in routes:
            dir, dist = w.split(" ")
            for i in range(1, int(dist) + 1):
                nr = str + (direction[dir][0] * i)
                nc = stc + (direction[dir][1] * i)
                if 0 <= nr < n and 0 <= nc < m and park[nr][nc] != "X":
                    continue
                else:
                    break
            else:
                str = nr
                stc = nc

        return [str, stc]

    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                return(move(i, j))
    return -1
