from collections import deque

def bfs(n):
    visited = [0] * maxV
    q = deque([n])
    while q:
        next = q.popleft()
        if next == k:   # next가 동생이 있는 위치일 경우
            return visited[next]
        for pos in (next-1, next+1, next*2):    # 현재 위치에서 갈 수 있는 경우의 수 2가지
            if 0 <= pos < maxV and not visited[pos]:    # 범위 설정 및 방문 확인
                visited[pos] = visited[next] + 1        # 다음 이동 칸에 현재칸 까지 걸린 시간에 1초를 더해 줌
                q.append(pos)

n, k = map(int, input().split())
maxV = 100001       # k의 최댓값 만큼 배열 생성
print(bfs(n))