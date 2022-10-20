from heapq import heappush, heappop

v, e = map(int, input().split())
graph = [[] * (v+1)]
for _ in range(e):
    st, ed, w = map(int, input().split())
    graph[st].append((ed, w))

