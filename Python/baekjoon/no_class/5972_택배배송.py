from heapq import heappush, heappop

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = int(1e9)
distance = [INF] * (n + 1)

def dijk():
    distance[1] = 0
    heap = []
    heappush(heap, (distance[1], 1))
    while heap:
        cur_val, cur = heappop(heap)
        if distance[cur] < cur_val:
            continue
        for next_node, next_value in graph[cur]:
            if distance[next_node] > distance[cur] + next_value:
                distance[next_node] = distance[cur] + next_value
                heappush(heap, (distance[next_node], next_node))

for _ in range(m):
    a, b, feed = map(int, input().split())
    graph[a].append((b, feed))
    graph[b].append((a, feed))

dijk()
print(distance[n])
