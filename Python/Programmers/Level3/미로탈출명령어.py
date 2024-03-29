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

'''
O(N) 풀이

def solution(n, m, x, y, r, c, k):
    answer = ''
    diff = abs(x-r)+abs(y-c)
    if diff % 2 != k % 2 or diff > k:
        return 'impossible'
    #dlru 순서

    rest = k - diff
    lcount = 0
    rcount = 0
    dcount = 0
    ucount = 0
    if x < r : #내려가야함
        dcount = r - x
    else:
        ucount = x - r
    if y < c :
        rcount = c - y
    else:
        lcount = y - c

    dplus = min(n-max(x,r), rest//2)
    rest -= dplus * 2

    lplus = min(min(y,c)-1, rest//2)
    rest -= lplus * 2

    answer = 'd' * (dcount+dplus) + 'l' * (lcount+lplus) + 'rl' * (rest//2) + 'r' * (rcount+lplus) + 'u' * (dplus+ucount)
    print(lcount, lplus, rcount, rest)

    return answer

'''
