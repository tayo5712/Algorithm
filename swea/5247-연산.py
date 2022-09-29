import sys
sys.stdin = open("input_5247.txt", "r")

from collections import deque

def bfs(n):
    visited = [0] * 1000001     # 최대 숫자 만큼 방문리스트 만들기
    q = deque()
    q.append((n, 0))            # 처음숫자랑 연산 횟수 append
    while q:
        num, cnt = q.popleft()
        if not visited[num]:    # 현제 연산된 숫자가 전에 연산한 숫자가 아니라면
            visited[num] = 1

            if num == m:        # 목표 숫자에 도달하면 연산횟수 반환
                return cnt

            else:
                cnt += 1        # 연산 횟수 1 증가
                if 0 <= num+1 <= 1000000:   # 연산한 숫자가 범위 안이면
                    q.append((num+1, cnt))
                if 0 <= num-1 <= 1000000:
                    q.append((num-1, cnt))
                if 0 <= num*2 <= 1000000:
                    q.append((num*2, cnt))
                if 0 <= num-10 <= 1000000:
                    q.append((num-10, cnt))


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())

    print(f'#{tc} {bfs(n)}')