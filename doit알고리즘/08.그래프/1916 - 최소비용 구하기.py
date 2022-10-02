from heapq import heappush, heappop

def dijk(start):
    value = [100000001] * (n + 1)
    visited = [0] * (n+1)
    value[start] = 0
    heappush(heap, (0, start))
    while heap:
        w, curV = heappop(heap)
        if not visited[curV]:
            visited[curV] = 1
            for nextW, nextV in graph[curV]:
                if not visited[nextV] and value[nextV] > nextW + w:
                    value[nextV] = nextW + w
                    heappush(heap, (value[nextV], nextV))
    return value[end]

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
heap = []
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
start, end = map(int, input().split())
print(dijk(start))


