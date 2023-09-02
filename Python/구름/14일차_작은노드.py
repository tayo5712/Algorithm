from collections import deque


def move(start):
    global cnt
    q = deque()
    q.append(start)
    while q:
        cur = q.popleft()
        for next in nodes[cur]:
            if not visited[next]:
                visited[next] = 1
                cnt += 1
                q.append(next)
                break
    return cur


N, M, K = map(int, input().split())
nodes = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
for node in nodes:
    node.sort()
visited = [0] * (N + 1)
visited[K] = 1
cnt = 1
answer = move(K)
print(cnt, answer)
