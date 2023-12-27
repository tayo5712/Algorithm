from collections import deque

def bfs(sti, stj, maps, n, m):
    # 다 돌았는데도 탈출 할 수 없다면 -1
    q = deque()
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[sti][stj] = 1
    q.append((sti, stj, 0))  # 세로좌표, 가로좌표, 카운트
    flag = False

    while q:
        i, j, cnt = q.popleft()
        for di, dj in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and maps[ni][nj] != "X":
                if maps[ni][nj] == "E":
                    if flag:
                        return cnt + 1
                # 레버 당기고 큐, 방문 배열 초기화
                elif maps[ni][nj] == "L":  # 레버일 경우
                    visited = [[0 for _ in range(m)] for _ in range(n)]
                    q = deque([(ni, nj, cnt + 1)])
                    visited[ni][nj] = 1
                    flag = True
                    break

                visited[ni][nj] = 1
                q.append((ni, nj, cnt + 1))

                
    return -1

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                answer = bfs(i, j, maps, n, m)

    return answer
