from collections import deque

def BFS(sti, stj):
    global result
    q = deque()
    q.append((sti, stj, 1, board[sti][stj]))
    while q:
        i, j, cnt, num = q.popleft()
        if cnt > 5:
            result.add(num)
        else:
            for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                ni = i + di
                nj = j + dj
                if 0 <= ni < 5 and 0 <= nj < 5:
                    q.append((ni, nj, cnt+1, num+board[ni][nj]))

board = [list(input().split()) for _ in range(5)]
result = set()
for i in range(5):
    for j in range(5):
        BFS(i, j)

print(len(result))