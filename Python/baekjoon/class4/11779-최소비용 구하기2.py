from heapq import heappop, heappush

# 다익스트라
def solved(st):
    heap = []
    path = [-1 for _ in range(n+1)] # 경로 저장
    value = [100000001 for _ in range(n+1)]
    visited = [0] * (n+1)
    value[st] = 0
    heappush(heap, (0, st))
    while heap:
        w, curV = heappop(heap)
        if not visited[curV]:
            visited[curV] = 1
            for nextV, nextW in graph[curV]:
                if not visited[nextV] and value[nextV] > nextW + w:
                    value[nextV] = nextW + w
                    path[nextV] = curV
                    heappush(heap, (value[nextV], nextV))

    return value, path

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
st, ed = map(int, input().split())
value, path = solved(st)

print(value[ed])
pathResult = []
# 경로 역추적
temp = ed
while temp != -1:
    pathResult.append(temp)
    temp = path[temp]

print(len(pathResult))
print(*pathResult[::-1])
