from collections import deque
def bfs(a, b):  # 계속 증가만 하기 때문에 visited 필요없음
    q = deque()
    q.append((a, 0))
    while q:
        a, cnt = q.popleft()
        if a == b:
            return cnt+1

        v1 = a * 2          # 2를 곱할 경우
        v2 = a * 10 + 1     # 오른쪽에 1 추가할 경우
        if v1 <= b:         # 목표 넘으면 볼 필요없음 수가 줄어드는 방법이 없기 때문에
            q.append((v1, cnt+1))
        if v2 <= b:
            q.append((v2, cnt+1))

    return -1

a, b = map(int, input().split())
print(bfs(a, b))