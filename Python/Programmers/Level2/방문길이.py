def solution(dirs):
    answer = 0
    str, stc = 5, 5
    move = {"U": [-1, 0], "D": [1, 0], "R": [0, 1], "L": [0, -1]}
    visited = [[[] for _ in range(11)] for _ in range(11)]
    for dir in dirs:
        nr = str + move[dir][0]
        nc = stc + move[dir][1]

        if 0 <= nr <= 10 and 0 <= nc <= 10:
            # 지나갔던 길인지
            if (str, stc) not in visited[nr][nc] and (nr, nc) not in visited[str][stc]:
                answer += 1
                visited[nr][nc].append((str, stc))
                visited[str][stc].append((nr, nc))
            str = nr
            stc = nc

    return answer


def solution(dirs):
    sets = set()
    y, x = 0, 0
    udrl = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}

    for d in dirs:
        dy, dx = udrl[d]
        ny = y + dy
        nx = x + dx
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            sets.add(((y, x), (ny, nx)))
            sets.add(((ny, nx), (y, x)))
            y = ny
            x = nx
    return len(sets) // 2