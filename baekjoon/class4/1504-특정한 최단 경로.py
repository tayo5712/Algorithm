from heapq import heappush, heappop

def dijk():
    value = [100000] * (v+1)
    value[1] = 0
    heap = []
    heappush(heap, (0, 0))
    while heap:
        w, curV = heappop(heap)
        for nextV, nextW in graph[curV]:
            if value[nextV] > nextW + w:
                value[nextV] = nextW + w
                heappush(heap, (value[nextV], nextV))
    return value

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    st, ed, w = map(int, input().split())
    graph[st].append((ed, w))
    graph[ed].append((st, w))
v1, v2 = map(int, input().split())
print(dijk())
