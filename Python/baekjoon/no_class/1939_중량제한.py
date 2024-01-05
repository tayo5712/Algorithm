from collections import deque

def bfs(max_weight):
    visited = [0] * (n + 1)
    visited[island1] = 1
    q = deque([island1])
    while q:
        now = q.popleft()
        for next, weight in island[now]:
            if not visited[next] and max_weight <= weight:
                if next == island2:
                    return True
                visited[next] = 1
                q.append(next)
    return False           

n, m = map(int, input().split())
island = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, weight = map(int, input().split())
    island[a].append((b, weight))
    island[b].append((a, weight))

result  = 0
island1, island2 = map(int, input().split())

st = 1
ed = 1000000000
while st <= ed:
    mid = (st + ed) // 2 # 옮기고자 하는 물품의 무게
    if bfs(mid):
        result = mid
        st = mid + 1
    else:
        ed = mid - 1

print(result)

