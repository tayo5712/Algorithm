from heapq import heappush, heappop

def dijk(start):
    global cnt
    value = [200001] * (n + 1)
    value[start] = 0
    heappush(heap, (0, start))
    while heap:

        w, curV = heappop(heap)
        for nextW, nextV in graph[curV]:
            if value[nextV] > nextW + w:
                value[nextV] = nextW + w
                heappush(heap, (value[nextV], nextV))
    return value

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
heap = []

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
result = dijk(start)

for i in range(1, n+1):
    if result[i] < 200001:
        print(result[i])
    else:
        print('INF')