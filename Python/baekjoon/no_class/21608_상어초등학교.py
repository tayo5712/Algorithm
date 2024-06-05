def set_pos(person):
    best_pos = [-1, -1]
    max_favorite = 0
    max_empty = 0
    for r in range(n):
        for c in range(n):
            close_favorite = 0
            close_empty = 0
            # 현재 위치에서 인접 한 곳 (4곳 확인)
            for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                if room[r][c] == 0: # 현재 자리 비어있을 때
                    near_r, near_c = r + dr, c + dc
                    if 0 <= near_r < n and 0 <= near_c < n:
                        if room[near_r][near_c] == 0:
                            close_empty += 1
                        elif room[near_r][near_c] in favorite[person]:
                            close_favorite += 1

            if (close_favorite > max_favorite) or (close_favorite == max_favorite and close_empty > max_empty):
                max_favorite = close_favorite
                max_empty = close_empty
                best_pos = [r, c]

            elif best_pos == [-1, -1] and room[r][c] == 0: # 최적의 자리가 없으면, 일단 비어있으면 앉힌다.
                best_pos = [r, c]
    room[best_pos[0]][best_pos[1]] = person

n = int(input())
favorite = {}
room = [[0 for _ in range(n)] for _ in range(n)]
answer = 0

for _ in range(n * n):
    me, *love = map(int, input().split())
    favorite[me] = set(love)
    set_pos(me)

for i in range(n):
    for j in range(n):
        close_favorite = 0
        for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            near_r = i + dr
            near_c = j + dc
            if 0 <= near_r < n and 0 <= near_c < n and room[near_r][near_c] in favorite[room[i][j]]:
                close_favorite += 1
        answer += round(10 ** (close_favorite - 1))
print(answer)


