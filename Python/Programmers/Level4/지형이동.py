from collections import deque
from heapq import heappush, heappop

answer = 0

def solution(land, height):  
    
    def bfs():
        global answer
        visited = [[0 for _ in range(n)] for _ in range(n)]
        visited[0][0] = 1
        ladder = []
        q = deque([(0, 0)])
        while q:
            rr, cc = q.popleft()
            for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nr = rr + dr
                nc = cc + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    differ = abs(land[rr][cc] - land[nr][nc])
                    if differ <= height:
                        visited[nr][nc] = 1
                        q.append((nr, nc))
                    else:
                        heappush(ladder, (differ, nr, nc))
            if not q:
                while ladder:
                    cost, lr, lc = heappop(ladder)
                    if not visited[lr][lc]:
                        visited[lr][lc] = 1
                        answer += cost
                        q.append((lr, lc))
                        break
    
    n = len(land) 
    bfs()
    return answer
    
    
