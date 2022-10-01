import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# 2차원 배열로 풀면 메모리 초과
# priorityqueue 쓰면 시간 초과
# heapqueue 만세세
def prim():
    heap = []
    check = [0] * (n+1)
    heappush(heap, (0, 1))
    cnt = 0
    result = 0
    while cnt < n:
        w, curV = heappop(heap)
        if not check[curV]:
            check[curV] = 1
            cnt += 1
            result += w
            for cost in graph[curV]:
                heappush(heap, cost)

    return result

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    st, ed, w = map(int, input().split())
    graph[st].append((w, ed))
    graph[ed].append((w, st))

print(prim())