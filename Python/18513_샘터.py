from collections import deque

n, k = map(int, input().split())
rest = list(map(int, input().split()))
k += len(rest)

visited = set()
q = deque()
for pos in rest:
    q.append((pos, 0))
    visited.add(pos)

answer = 0
while q and k > 0:
    tp, dist = q.popleft()
    answer += dist
    k -= 1
    for di in (-1, 1):
        np = tp + di
        if np not in visited:
            q.append((np, dist + 1))
            visited.add(np)
print(answer)
