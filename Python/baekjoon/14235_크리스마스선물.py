from heapq import heappush, heappop

n = int(input())
heap = []
for _ in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0:
        if len(heap) > 0:
            print(heappop(heap)[1])
        else:
            print(-1)
    else:
        for i in a[1:]:
            heappush(heap, (-i, i))

