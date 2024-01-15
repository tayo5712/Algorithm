from collections import deque

def solution(n, m, x, y, r, c, k):

    r -= 1 # 인덱스랑 맞춰주려고
    c -= 1
    x -= 1
    y -= 1

    def bfs():
        dr = [1, 0, 0, -1] # 하, 좌, 우, 상  사전순서때문에
        dc = [0, -1, 1, 0]
        letter = ["d", "l", "r", "u"]
        
        visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(k + 1)]
        visited[0][r][c] = 1
        
        q = deque()
        q.append((x, y, 0, ""))
        while q:
            lr, lc, cnt, word = q.popleft()
            if cnt == k and lr == r and lc == c:
                return word
            else:
                for i in range(4):
                    nr = lr + dr[i]
                    nc = lc + dc[i]
                    if 0 <= nr < n and 0 <= nc < m and abs(nr-r) + abs(nc-c) <= k - (cnt + 1) and not visited[cnt + 1][nr][nc]:
                        q.append((nr, nc, cnt + 1, word + letter[i]))
                        visited[cnt + 1][nr][nc] = 1
        return "impossible"

    return bfs()

