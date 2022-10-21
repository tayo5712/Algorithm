import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def prim():
    check = [0] * n
    value = [1000000000] * n
    value[0] = 0
    heap = []
    heappush(heap, (0, 0))
    while heap:
        w, curV = heappop(heap)
        if not check[curV]:
            check[curV] = 1
            for nextV, nextW in graph[curV]:
                if not check[nextV] and value[nextV] > nextW:
                    value[nextV] = nextW
                    heappush(heap, (nextW, nextV))
    return sum(value)

n = int(input())
graph = [[] for _ in range(n)]
x = []
y = []
z = []
for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))
x.sort()
y.sort()
z.sort()

for i in range(n-1):
    graph[x[i][1]].append((x[i + 1][1], abs(x[i + 1][0] - x[i][0])))
    graph[x[i + 1][1]].append((x[i][1], abs(x[i + 1][0] - x[i][0])))

    graph[y[i][1]].append((y[i + 1][1], abs(y[i + 1][0] - y[i][0])))
    graph[y[i + 1][1]].append((y[i][1], abs(y[i + 1][0] - y[i][0])))

    graph[z[i][1]].append((z[i + 1][1], abs(z[i + 1][0] - z[i][0])))
    graph[z[i + 1][1]].append((z[i][1], abs(z[i + 1][0] - z[i][0])))

print(prim())

